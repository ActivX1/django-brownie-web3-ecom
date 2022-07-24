// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract Sales{

    mapping(address=>uint256) public addressToAmountFunded;
    address[] public funders;
    address public owner;

    constructor() {
        owner = msg.sender;
    }


    function getContractBalance() public view returns (uint256){
        return (address(this).balance);
    }

    function makePayment() public payable{
        addressToAmountFunded[msg.sender] = msg.value;
        funders.push(msg.sender);
    }


    modifier onlyOwner{
        require(msg.sender==owner);
        _;
    }

    function withdrawfromContract() public onlyOwner payable{
        payable(msg.sender).transfer(address(this).balance);
        for (uint funderIndex=0; funderIndex< funders.length; funderIndex++){
            addressToAmountFunded[funders[funderIndex]]=0;
        }
        funders = new address[](0);
    }

    fallback() external payable {}
    receive() external payable {}

}

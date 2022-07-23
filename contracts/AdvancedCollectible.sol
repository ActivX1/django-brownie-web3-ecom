// SPDX-License-Identifier: MIT
pragma solidity ^0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract AdvancedCollectible is ERC721 {
    uint256 public tokenCounter;
    constructor() public ERC721("ProductNFT", "PNFT") {
        tokenCounter = 0;
    }

    function createCollectible() public returns (uint256){
        uint256 newTokenId = tokenCounter;
        _safeMint(msg.sender, newTokenId);
        tokenCounter = tokenCounter + 1;
        return newTokenId;
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
        require(_isApprovedOrOwner(_msgSender(), tokenId), "ERC721: caller is not owner or not approved");
        _setTokenURI(tokenId, _tokenURI);
    }
}
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="CE407 - Blockchain & Cryptocurrency", page_icon="⛓️", layout="wide")

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=JetBrains+Mono&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    code, pre {
        font-family: 'JetBrains Mono', monospace !important;
    }
    
    .course-header {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: white;
        padding: 2.5rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    .course-title {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    
    .theory-box {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border-left: 5px solid #f59e0b;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .bitcoin-box {
        background: linear-gradient(135deg, #fed7aa 0%, #fdba74 100%);
        border-left: 5px solid #ea580c;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .ethereum-box {
        background: linear-gradient(135deg, #ddd6fe 0%, #c4b5fd 100%);
        border-left: 5px solid #8b5cf6;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .defi-box {
        background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
        border-left: 5px solid #10b981;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .youtube-box {
        background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
        border-left: 5px solid #ef4444;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="course-header">
    <div style="font-size: 1.2rem; opacity: 0.9;">CE407</div>
    <div class="course-title">Blockchain & Cryptocurrency</div>
    <div>⛓️ 3 Credits | Semester 8 | Bitcoin, Ethereum, Smart Contracts & DeFi</div>
</div>
""", unsafe_allow_html=True)

# Course Info
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Credits", "3")
with col2:
    st.metric("Semester", "8")
with col3:
    st.metric("Difficulty", "6/7")
with col4:
    st.metric("Hours/Week", "7")

st.markdown("---")

# Navigation tabs
tabs = st.tabs([
    "📚 Overview",
    "⛓️ Blockchain Basics",
    "₿ Bitcoin",
    "⟠ Ethereum & Smart Contracts",
    "💰 DeFi",
    "🎨 NFTs",
    "🔐 Consensus & Security",
    "📺 YouTube Resources"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.markdown("## 📚 Course Overview")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Course Description</h3>
        <p>Comprehensive blockchain and cryptocurrency course covering distributed ledger technology, cryptographic principles, 
        Bitcoin, Ethereum, smart contracts, DeFi, NFTs, and consensus mechanisms. Learn blockchain architecture, cryptocurrency 
        economics, Solidity programming, decentralized applications (dApps), and blockchain security. Emphasizes hands-on 
        development with real blockchain networks. Students will build smart contracts, deploy dApps, and understand the 
        economic and social implications of blockchain technology.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Learning Outcomes")
    
    outcomes = [
        "Understand blockchain architecture and cryptographic foundations",
        "Explain Bitcoin's proof-of-work and transaction model",
        "Write and deploy smart contracts in Solidity",
        "Build decentralized applications (dApps) on Ethereum",
        "Understand DeFi protocols (lending, DEX, yield farming)",
        "Create and trade NFTs on blockchain networks",
        "Analyze consensus mechanisms (PoW, PoS, BFT)",
        "Evaluate blockchain security and attack vectors"
    ]
    
    for outcome in outcomes:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("### 📋 Course Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Blockchain Fundamentals:**
        - Distributed ledger technology
        - Cryptographic hash functions
        - Digital signatures (ECDSA)
        - Merkle trees
        - Consensus algorithms
        
        **Bitcoin:**
        - Bitcoin protocol
        - UTXO model
        - Mining and proof-of-work
        - Bitcoin scripting
        - Lightning Network
        """)
    
    with col2:
        st.markdown("""
        **Ethereum & Smart Contracts:**
        - Ethereum Virtual Machine (EVM)
        - Solidity programming
        - Gas and transaction fees
        - ERC-20, ERC-721 tokens
        - Web3.js and ethers.js
        
        **DeFi & Applications:**
        - Decentralized exchanges (Uniswap)
        - Lending protocols (Aave, Compound)
        - Stablecoins (USDC, DAI)
        - NFT marketplaces
        - DAOs (Decentralized Autonomous Organizations)
        """)
    
    st.markdown("### 📚 Recommended Resources")
    
    resources = [
        {"title": "Mastering Bitcoin", "author": "Andreas Antonopoulos", "type": "Bitcoin"},
        {"title": "Mastering Ethereum", "author": "Antonopoulos & Wood", "type": "Ethereum"},
        {"title": "The Infinite Machine", "author": "Camila Russo", "type": "Ethereum History"},
        {"title": "Solidity Documentation", "author": "Ethereum Foundation", "type": "Smart Contracts"}
    ]
    
    for resource in resources:
        title = resource['title']
        author = resource['author']
        rtype = resource['type']
        st.markdown(f"📖 **{title}** by {author} ({rtype})")

# ==================== TAB 2: BLOCKCHAIN BASICS ====================
with tabs[1]:
    st.markdown("## ⛓️ Blockchain Basics")
    
    st.markdown("### 1️⃣ What is Blockchain?")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Key Concepts:</strong><br><br>
        
        <strong>Distributed Ledger:</strong><br>
        • Shared database across network<br>
        • No central authority<br>
        • Transparent and immutable<br>
        • Cryptographically secured<br><br>
        
        <strong>Block Structure:</strong><br>
        • <strong>Block Header:</strong> Previous hash, timestamp, nonce, Merkle root<br>
        • <strong>Block Body:</strong> List of transactions<br>
        • <strong>Hash:</strong> Unique identifier (SHA-256)<br><br>
        
        <strong>Chain of Blocks:</strong><br>
        • Each block references previous block's hash<br>
        • Tampering with one block invalidates all subsequent blocks<br>
        • Immutability through cryptographic linking<br><br>
        
        <strong>Properties:</strong><br>
        • <strong>Decentralization:</strong> No single point of failure<br>
        • <strong>Transparency:</strong> All transactions visible<br>
        • <strong>Immutability:</strong> Cannot alter past records<br>
        • <strong>Security:</strong> Cryptographic protection
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Cryptographic Foundations")
    
    st.markdown("""
    <div class="bitcoin-box">
        <strong>Hash Functions (SHA-256):</strong><br>
        <pre>
import hashlib

# Hash a message
message = "Hello, Blockchain!"
hash_object = hashlib.sha256(message.encode())
hash_hex = hash_object.hexdigest()
print(hash_hex)
# Output: 256-bit hash (64 hex characters)
        </pre><br>
        
        <strong>Properties:</strong><br>
        • Deterministic (same input → same output)<br>
        • Fast to compute<br>
        • Avalanche effect (small change → completely different hash)<br>
        • Collision resistant<br>
        • One-way (cannot reverse)<br><br>
        
        <strong>Digital Signatures (ECDSA):</strong><br>
        • Public/private key pairs<br>
        • Sign with private key<br>
        • Verify with public key<br>
        • Proves ownership and authenticity<br><br>
        
        <strong>Merkle Trees:</strong><br>
        • Binary tree of hashes<br>
        • Efficient verification of data integrity<br>
        • Used in Bitcoin blocks<br>
        • Allows SPV (Simplified Payment Verification)
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 3: BITCOIN ====================
with tabs[2]:
    st.markdown("## ₿ Bitcoin")
    
    st.markdown("### 1️⃣ Bitcoin Architecture")
    
    st.markdown("""
    <div class="bitcoin-box">
        <strong>UTXO Model:</strong><br>
        • Unspent Transaction Output<br>
        • No account balances<br>
        • Transactions consume inputs, create outputs<br>
        • Outputs become inputs for future transactions<br><br>
        
        <strong>Transaction Structure:</strong><br>
        <pre>
{
  "version": 1,
  "inputs": [
    {
      "previous_tx": "abc123...",
      "output_index": 0,
      "script_sig": "signature + public_key"
    }
  ],
  "outputs": [
    {
      "value": 0.5,  // BTC
      "script_pubkey": "OP_DUP OP_HASH160 <pubkey_hash> OP_EQUALVERIFY OP_CHECKSIG"
    }
  ],
  "locktime": 0
}
        </pre><br>
        
        <strong>Bitcoin Address:</strong><br>
        • Public key → SHA-256 → RIPEMD-160 → Base58Check<br>
        • Example: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa<br>
        • SegWit addresses start with bc1
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Mining & Proof-of-Work")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Mining Process:</strong><br>
        1. Collect pending transactions<br>
        2. Create block header<br>
        3. Find nonce such that hash(block) < target<br>
        4. Broadcast block to network<br>
        5. Receive block reward + transaction fees<br><br>
        
        <strong>Proof-of-Work:</strong><br>
        <pre>
import hashlib

def mine_block(block_data, difficulty):
    target = "0" * difficulty
    nonce = 0
    
    while True:
        block = f"{block_data}{nonce}"
        hash_result = hashlib.sha256(block.encode()).hexdigest()
        
        if hash_result.startswith(target):
            return nonce, hash_result
        
        nonce += 1

# Example: mine block with 4 leading zeros
data = "Block #123: Alice -> Bob: 1 BTC"
nonce, hash_val = mine_block(data, difficulty=4)
print(f"Nonce: {nonce}, Hash: {hash_val}")
        </pre><br>
        
        <strong>Difficulty Adjustment:</strong><br>
        • Target: 1 block every 10 minutes<br>
        • Adjusts every 2016 blocks (~2 weeks)<br>
        • Maintains consistent block time<br><br>
        
        <strong>Block Reward:</strong><br>
        • Started at 50 BTC (2009)<br>
        • Halves every 210,000 blocks (~4 years)<br>
        • Current: 6.25 BTC (as of 2024)<br>
        • Max supply: 21 million BTC
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 4: ETHEREUM ====================
with tabs[3]:
    st.markdown("## ⟠ Ethereum & Smart Contracts")
    
    st.markdown("### 1️⃣ Solidity Basics")
    
    st.markdown("""
    <div class="ethereum-box">
        <strong>Simple Smart Contract:</strong><br>
        <pre>
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 private storedData;
    
    event DataStored(uint256 newValue);
    
    function set(uint256 x) public {
        storedData = x;
        emit DataStored(x);
    }
    
    function get() public view returns (uint256) {
        return storedData;
    }
}
        </pre><br>
        
        <strong>ERC-20 Token:</strong><br>
        <pre>
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MyToken is ERC20 {
    constructor(uint256 initialSupply) ERC20("MyToken", "MTK") {
        _mint(msg.sender, initialSupply);
    }
}
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Advanced Solidity")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Voting Contract:</strong><br>
        <pre>
pragma solidity ^0.8.0;

contract Voting {
    struct Proposal {
        string description;
        uint256 voteCount;
    }
    
    mapping(address => bool) public hasVoted;
    Proposal[] public proposals;
    
    constructor(string[] memory proposalDescriptions) {
        for (uint i = 0; i < proposalDescriptions.length; i++) {
            proposals.push(Proposal({
                description: proposalDescriptions[i],
                voteCount: 0
            }));
        }
    }
    
    function vote(uint256 proposalIndex) public {
        require(!hasVoted[msg.sender], "Already voted");
        require(proposalIndex < proposals.length, "Invalid proposal");
        
        hasVoted[msg.sender] = true;
        proposals[proposalIndex].voteCount++;
    }
    
    function winningProposal() public view returns (uint256) {
        uint256 winningVoteCount = 0;
        uint256 winningIndex = 0;
        
        for (uint i = 0; i < proposals.length; i++) {
            if (proposals[i].voteCount > winningVoteCount) {
                winningVoteCount = proposals[i].voteCount;
                winningIndex = i;
            }
        }
        
        return winningIndex;
    }
}
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Web3.js Integration")
    
    st.markdown("""
    <div class="ethereum-box">
        <strong>Connect to Ethereum:</strong><br>
        <pre>
const Web3 = require('web3');
const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_API_KEY');

// Get balance
const balance = await web3.eth.getBalance('0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb');
console.log(web3.utils.fromWei(balance, 'ether'));

// Interact with contract
const contractABI = [...]; // Contract ABI
const contractAddress = '0x...';
const contract = new web3.eth.Contract(contractABI, contractAddress);

// Call view function
const value = await contract.methods.get().call();

// Send transaction
const accounts = await web3.eth.getAccounts();
await contract.methods.set(42).send({ from: accounts[0] });
        </pre>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 5: DEFI ====================
with tabs[4]:
    st.markdown("## 💰 DeFi (Decentralized Finance)")
    
    st.markdown("### 1️⃣ DeFi Protocols")
    
    defi_data = {
        'Protocol': ['Uniswap', 'Aave', 'Compound', 'MakerDAO', 'Curve'],
        'Type': ['DEX', 'Lending', 'Lending', 'Stablecoin', 'DEX'],
        'Description': [
            'Automated market maker (AMM)',
            'Decentralized lending/borrowing',
            'Algorithmic money market',
            'DAI stablecoin protocol',
            'Stablecoin exchange'
        ],
        'TVL (Billions)': ['$4B', '$6B', '$3B', '$5B', '$2B']
    }
    
    df_defi = pd.DataFrame(defi_data)
    st.dataframe(df_defi, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Automated Market Maker (AMM)")
    
    st.markdown("""
    <div class="defi-box">
        <strong>Constant Product Formula (Uniswap):</strong><br>
        x * y = k<br><br>
        
        • x: Token A reserves<br>
        • y: Token B reserves<br>
        • k: Constant product<br><br>
        
        <strong>Example:</strong><br>
        Pool: 100 ETH, 200,000 USDC<br>
        k = 100 * 200,000 = 20,000,000<br><br>
        
        Swap 10 ETH for USDC:<br>
        • New ETH: 110<br>
        • New USDC: 20,000,000 / 110 = 181,818<br>
        • USDC received: 200,000 - 181,818 = 18,182<br>
        • Price: 1,818 USDC per ETH<br><br>
        
        <strong>Liquidity Providers:</strong><br>
        • Deposit equal value of both tokens<br>
        • Receive LP tokens<br>
        • Earn trading fees (0.3%)<br>
        • Risk: Impermanent loss
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Lending & Borrowing")
    
    st.markdown("""
    <div class="theory-box">
        <strong>How it Works:</strong><br><br>
        
        <strong>Lending:</strong><br>
        1. Deposit collateral (e.g., ETH)<br>
        2. Earn interest on deposits<br>
        3. Receive aTokens (Aave) or cTokens (Compound)<br>
        4. Withdraw anytime<br><br>
        
        <strong>Borrowing:</strong><br>
        1. Deposit collateral<br>
        2. Borrow up to collateral ratio (e.g., 75%)<br>
        3. Pay interest on borrowed amount<br>
        4. Risk: Liquidation if collateral drops<br><br>
        
        <strong>Interest Rates:</strong><br>
        • Algorithmic (supply/demand)<br>
        • Variable rates<br>
        • Utilization ratio determines rate<br><br>
        
        <strong>Liquidation:</strong><br>
        • Occurs when collateral < threshold<br>
        • Liquidators repay debt, receive collateral + bonus<br>
        • Protects protocol solvency
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 6: NFTS ====================
with tabs[5]:
    st.markdown("## 🎨 NFTs (Non-Fungible Tokens)")
    
    st.markdown("### 1️⃣ ERC-721 Standard")
    
    st.markdown("""
    <div class="ethereum-box">
        <strong>NFT Smart Contract:</strong><br>
        <pre>
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract MyNFT is ERC721 {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;
    
    mapping(uint256 => string) private _tokenURIs;
    
    constructor() ERC721("MyNFT", "MNFT") {}
    
    function mintNFT(address recipient, string memory tokenURI) 
        public returns (uint256) 
    {
        _tokenIds.increment();
        uint256 newItemId = _tokenIds.current();
        
        _mint(recipient, newItemId);
        _tokenURIs[newItemId] = tokenURI;
        
        return newItemId;
    }
    
    function tokenURI(uint256 tokenId) 
        public view override returns (string memory) 
    {
        return _tokenURIs[tokenId];
    }
}
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ NFT Metadata")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Metadata JSON (IPFS):</strong><br>
        <pre>
{
  "name": "My Awesome NFT #1",
  "description": "This is a unique digital artwork",
  "image": "ipfs://QmX...",
  "attributes": [
    {
      "trait_type": "Background",
      "value": "Blue"
    },
    {
      "trait_type": "Rarity",
      "value": "Legendary"
    }
  ]
}
        </pre><br>
        
        <strong>Use Cases:</strong><br>
        • Digital art and collectibles<br>
        • Gaming items and characters<br>
        • Virtual real estate (metaverse)<br>
        • Music and media rights<br>
        • Event tickets<br>
        • Domain names (ENS)<br><br>
        
        <strong>NFT Marketplaces:</strong><br>
        • OpenSea (largest)<br>
        • Rarible<br>
        • Foundation<br>
        • SuperRare<br>
        • LooksRare
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 7: CONSENSUS ====================
with tabs[6]:
    st.markdown("## 🔐 Consensus & Security")
    
    st.markdown("### 1️⃣ Consensus Mechanisms")
    
    consensus_data = {
        'Mechanism': ['Proof-of-Work', 'Proof-of-Stake', 'Delegated PoS', 'Byzantine Fault Tolerance'],
        'Used By': ['Bitcoin, Ethereum (old)', 'Ethereum 2.0, Cardano', 'EOS, Tron', 'Hyperledger, Cosmos'],
        'Energy': ['Very High', 'Low', 'Low', 'Low'],
        'Security': ['Very High', 'High', 'Medium', 'High'],
        'Throughput': ['Low (7 tps)', 'Medium (30 tps)', 'High (4000 tps)', 'High']
    }
    
    df_consensus = pd.DataFrame(consensus_data)
    st.dataframe(df_consensus, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Attack Vectors")
    
    st.markdown("""
    <div class="bitcoin-box">
        <strong>51% Attack:</strong><br>
        • Attacker controls >50% of network hash power<br>
        • Can double-spend coins<br>
        • Cannot steal coins or change consensus rules<br>
        • Very expensive on large networks (Bitcoin)<br><br>
        
        <strong>Smart Contract Vulnerabilities:</strong><br><br>
        
        <strong>Reentrancy Attack:</strong><br>
        <pre>
// Vulnerable contract
function withdraw() public {
    uint amount = balances[msg.sender];
    (bool success, ) = msg.sender.call{value: amount}("");
    require(success);
    balances[msg.sender] = 0;  // Too late!
}

// Fix: Checks-Effects-Interactions pattern
function withdraw() public {
    uint amount = balances[msg.sender];
    balances[msg.sender] = 0;  // Update state first
    (bool success, ) = msg.sender.call{value: amount}("");
    require(success);
}
        </pre><br>
        
        <strong>Integer Overflow/Underflow:</strong><br>
        • Use SafeMath library or Solidity 0.8+<br>
        • Built-in overflow checks in 0.8+<br><br>
        
        <strong>Front-Running:</strong><br>
        • Miners see pending transactions<br>
        • Can insert their own transaction first<br>
        • Mitigation: Commit-reveal schemes
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 8: YOUTUBE ====================
with tabs[7]:
    st.markdown("## 📺 YouTube Learning Resources")
    
    st.markdown("""
    <div class="youtube-box">
        <h3>🎓 Curated YouTube Channels & Playlists</h3>
        <p>High-quality video tutorials for learning Blockchain & Cryptocurrency</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Beginner Level
    st.markdown("### 🟢 Beginner Level")
    
    beginner_resources = [
        {"title": "Blockchain Explained", "channel": "Simply Explained", "url": "https://www.youtube.com/watch?v=SSo_EIwHSd4", "description": "Blockchain basics", "duration": "~5 min"},
        {"title": "Bitcoin & Cryptocurrency", "channel": "99Bitcoins", "url": "https://www.youtube.com/c/Bitcoinwithpaypal", "description": "Crypto fundamentals", "duration": "Channel"},
        {"title": "How Bitcoin Works", "channel": "3Blue1Brown", "url": "https://www.youtube.com/watch?v=bBC-nXj3Ng4", "description": "Visual explanation", "duration": "~26 min"}
    ]
    
    for resource in beginner_resources:
        title = resource['title']
        channel = resource['channel']
        url = resource['url']
        description = resource['description']
        duration = resource['duration']
        st.markdown(f"**[{title}]({url})**  \n📺 Channel: {channel} | ⏱️ {duration}  \n{description}")
        st.markdown("---")
    
    # Intermediate Level
    st.markdown("### 🟡 Intermediate Level")
    
    intermediate_resources = [
        {"title": "Solidity Tutorial", "channel": "freeCodeCamp.org", "url": "https://www.youtube.com/watch?v=M576WGiDBdQ", "description": "Complete Solidity course", "duration": "~16 hours"},
        {"title": "Smart Contract Development", "channel": "Dapp University", "url": "https://www.youtube.com/c/DappUniversity", "description": "Ethereum development", "duration": "Channel"},
        {"title": "DeFi Explained", "channel": "Finematics", "url": "https://www.youtube.com/c/Finematics", "description": "DeFi protocols", "duration": "Channel"}
    ]
    
    for resource in intermediate_resources:
        title = resource['title']
        channel = resource['channel']
        url = resource['url']
        description = resource['description']
        duration = resource['duration']
        st.markdown(f"**[{title}]({url})**  \n📺 Channel: {channel} | ⏱️ {duration}  \n{description}")
        st.markdown("---")
    
    # Advanced Level
    st.markdown("### 🔴 Advanced Level")
    
    advanced_resources = [
        {"title": "Advanced Solidity", "channel": "Smart Contract Programmer", "url": "https://www.youtube.com/c/SmartContractProgrammer", "description": "Advanced patterns", "duration": "Channel"},
        {"title": "Blockchain Security", "channel": "Trail of Bits", "url": "https://www.youtube.com/c/TrailofBits", "description": "Security audits", "duration": "Channel"},
        {"title": "Ethereum Core Dev", "channel": "Ethereum Foundation", "url": "https://www.youtube.com/c/EthereumFoundation", "description": "Protocol development", "duration": "Channel"}
    ]
    
    for resource in advanced_resources:
        title = resource['title']
        channel = resource['channel']
        url = resource['url']
        description = resource['description']
        duration = resource['duration']
        st.markdown(f"**[{title}]({url})**  \n📺 Channel: {channel} | ⏱️ {duration}  \n{description}")
        st.markdown("---")
    
    # Study Tips
    st.markdown("### 💡 Study Tips")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Recommended Learning Path:</strong><br>
        1. Understand blockchain fundamentals<br>
        2. Learn cryptography basics<br>
        3. Study Bitcoin architecture<br>
        4. Learn Solidity and smart contracts<br>
        5. Build dApps with Web3.js<br>
        6. Explore DeFi protocols<br>
        7. Practice security auditing<br>
        8. Stay updated with latest developments<br><br>
        
        <strong>Essential Tools:</strong><br>
        • <strong>Development:</strong> Remix IDE, Hardhat, Truffle<br>
        • <strong>Wallets:</strong> MetaMask, Ledger, Trust Wallet<br>
        • <strong>Networks:</strong> Ethereum, Polygon, Binance Smart Chain<br>
        • <strong>Testing:</strong> Ganache, Testnet faucets<br>
        • <strong>Libraries:</strong> Web3.js, ethers.js, OpenZeppelin<br><br>
        
        <strong>Career Paths:</strong><br>
        • Blockchain Developer<br>
        • Smart Contract Engineer<br>
        • DeFi Developer<br>
        • Blockchain Security Auditor<br>
        • Cryptocurrency Analyst<br>
        • Web3 Developer
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>CE407 - Blockchain & Cryptocurrency</strong><br>
    <small>UTel University | Computer Engineering Program</small>
</div>
""", unsafe_allow_html=True)

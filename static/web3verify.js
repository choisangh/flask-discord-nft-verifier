var discordId = "{{ discordId }}";
window.walletAddress = null;
const syncDiscord = document.getElementById("syncDiscord");
const connectWallet = document.getElementById("connectWallet");
const walletAddress = document.getElementById("walletAddress");

function checkInstalled() {
  if (typeof window.ethereum == "undefined") {
    walletAddress.innerText = "Please install MetaMask to continue.";
    return false;
  }
  connectWallet.addEventListener("click", connectWalletwithMetaMask);
}

async function connectWalletwithMetaMask() {
  const accounts = await window.ethereum
    .request({ method: "eth_requestAccounts" })
    .catch((e) => {
      console.error(e.message);
      return;
    });
  if (!accounts) {
    return;
  }

  window.walletAddress = accounts[0];
  walletAddress.innerText = window.walletAddress;

  connectWallet.innerText = "Sign Out";
  connectWallet.removeEventListener("click", connectWalletwithMetaMask);
  setTimeout(() => {
    connectWallet.addEventListener("click", signOutOfMetaMask);
    syncDiscord.addEventListener("click", syncDiscordWithWallet);
  }, 200);
}

function signOutOfMetaMask() {
  window.walletAddress = null;
  walletAddress.innerText = "";
  connectWallet.innerText = "Connect Wallet";

  connectWallet.removeEventListener("click", signOutOfMetaMask);
  syncDiscord.removeEventListener("click", syncDiscordWithWallet);

  setTimeout(() => {
    connectWallet.addEventListener("click", connectWalletwithMetaMask);
  }, 200);
}

window.addEventListener("DOMContentLoaded", () => {
  checkInstalled();
});

async function syncDiscordWithWallet() {
  if (!window.walletAddress) {
    walletAddress.innerText = "Please connect MetaMask to continue.";
    return false;
  }

  const message = `Discord ID: ${discordId} Wallet Address: ${window.walletAddress}`;
  const signature = await window.ethereum.request({
    method: "personal_sign",
    params: [message, window.walletAddress],
  });

  $.ajax({
    type: "POST",
    url: "/verify",
    data: {
        discordid: discordId,
        signature: signature,
        wallet: window.walletAddress,
        message: message
    },
    success: function(response) {
        console.log(response);
        alert(response);
    },
    error: function(xhr) {
        console.log(xhr);
        alert("Error occurred: " + xhr.statusText);
    }
});
}
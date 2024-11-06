function copyCurrentUrlToClipboard() {
    const currentUrl = window.location.href;
    const tempInput = document.createElement('input');
    tempInput.value = currentUrl;
    document.body.appendChild(tempInput);
    tempInput.select();
    document.execCommand('copy');
    document.body.removeChild(tempInput);
    alert('URL copied to clipboard!');
}

document.addEventListener('DOMContentLoaded', function() {
    if (!localStorage.getItem('hasVisitedBefore')) {
        openModal('howto-modal');
        localStorage.setItem('hasVisitedBefore', 'true');
    }
});

function openModal(modalId) {
    const modal = document.getElementById(modalId);
    modal.style.display = 'flex';
}

function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    modal.style.display = 'none';
}

document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        const modals = document.querySelectorAll('[id*="-modal"]');
        modals.forEach(modal => {
            modal.style.display = 'none';
        });
    }
});

function updateCountdown() {
    const now = new Date();
    const nextDay = new Date(now.getFullYear(), now.getMonth(), now.getDate() + 1);
    const diff = nextDay - now;

    const hours = Math.floor(diff / (1000 * 60 * 60));
    const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((diff % (1000 * 60)) / 1000);

    // Ensure countdown-timer exists
    const countdownElement = document.getElementById('countdown-timer');
    if (countdownElement) {
        countdownElement.innerText = `${hours}h ${minutes}m ${seconds}s`;
    }

    if (diff > 0) {
        setTimeout(updateCountdown, 1000);
    }
}

updateCountdown();
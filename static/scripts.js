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
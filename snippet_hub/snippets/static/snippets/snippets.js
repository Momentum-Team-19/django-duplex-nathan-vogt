// Path: snippet_hub/snippets/static/snippets/snippets.js

// Copy Snippet code and show the "Code copied!" message
async function copySnippetToClipboard(snippetId) {
    // Get the textarea that holds the code snippet
    const snippetCode = document.getElementById("snippetCode" + snippetId);
    
    // Select the content
    snippetCode.select();
    snippetCode.setSelectionRange(0, 99999);  // For mobile devices

    // Copy the text inside the text field to clipboard
    document.execCommand("copy");

    // Show the "Code copied!" message
  document.getElementById(`copyNotification_${snippetId}`).style.display = 'inline';

  // Optionally, make it disappear after a few seconds
  setTimeout(() => {
    document.getElementById(`copyNotification_${snippetId}`).style.display = 'none';
  }, 3000);

  // Making a request to the Django backend to increment the copy count
  const response = await fetch(`/increment_copy_count/${snippetId}/`);
  const data = await response.json();

  if (data.status === 'success') {
      // alert("Copied the code to clipboard");

      // Update "times copied" on the frontend
      const timesCopiedElement = document.getElementById(`copyCount${snippetId}`);
      let currentCount = parseInt(timesCopiedElement.textContent, 10);
      currentCount += 1;
      timesCopiedElement.textContent = currentCount;
  } else {
      alert("Could not increment copy count");
  }
}

// Autoresize textarea
var textArea = document.querySelector('.textarea-autoresize');
textArea.addEventListener('input', function () {
    this.style.height = 'auto';
    this.style.height = (this.scrollHeight) + 'px';
});
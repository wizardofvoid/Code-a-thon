function handleFile() {
    const fileInput = document.getElementById('csvFile');
    const file = fileInput.files[0];
    
    if (!file) {
        alert('Please select a CSV file.');
        return;
    }

    if (file.type !== 'text/csv') {
        alert('Please upload a valid CSV file.');
        return;
    }

    const reader = new FileReader();
    
    reader.onload = function(event) {
        const contents = event.target.result;
        alert('File Contents:\n' + contents);
    };

    reader.onerror = function() {
        alert('Error reading file.');
    };

    reader.readAsText(file);
}

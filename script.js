document.getElementById('conversionForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const temperature = document.getElementById('temperature').value;
    const unit = document.getElementById('unit').value;
    
    fetch('/convert', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ temperature: temperature, unit: unit })
    })
    .then(response => response.json())
    .then(data => {
        let result = 'Converted Temperatures:<br>';
        if (data.celsius !== undefined) result += `Celsius: ${data.celsius.toFixed(2)}°C<br>`;
        if (data.fahrenheit !== undefined) result += `Fahrenheit: ${data.fahrenheit.toFixed(2)}°F<br>`;
        if (data.kelvin !== undefined) result += `Kelvin: ${data.kelvin.toFixed(2)}K<br>`;
        document.getElementById('result').innerHTML = result;
    })
    .catch(error => console.error('Error:', error));
});

function getBathValue() {
  var bath = document.getElementById("bath").value;
  return parseInt(bath); // Returns the selected value from dropdown
}

function getBHKValue() {
  var bhk = document.getElementById("bhk").value;
  return parseInt(bhk); // Returns the selected value from dropdown
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");

  var sqft = document.getElementById("uiSqft").value;  // Get the square feet input
  var bhk = getBHKValue();  // Get the selected BHK value
  var bathrooms = getBathValue();  // Get the selected bath value
  var location = document.getElementById("uiLocations").value;  // Get the selected location
  var estPrice = document.getElementById("uiEstimatedPrice");  // Element to display estimated price

  var url = "http://127.0.0.1:5000/predict_home_price"; 

  // Call the API using jQuery's post method
  $.ajax({
    url: url,
    type: 'POST',
    contentType: 'application/json',  // Sending data as JSON
    dataType: 'json',  // Expecting JSON response
    data: JSON.stringify({
      total_sqft: parseFloat(sqft),
      bhk: bhk,
      bath: bathrooms,
      location: location
    }),
    success: function(data, status) {
      console.log("Estimated Price: " + data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";  // Display the estimated price
    },
    error: function(xhr, status, error) {
      console.error("Error: " + xhr.responseText);  // Log any error that occurs
    }
  });
}

function onPageLoad() {
  console.log("Document loaded");
  var url = "http://127.0.0.1:5000/get_location_names"; 

  $.get(url, function(data, status) {
    console.log("Got response for get_location_names request");
    if (data) {
      var locations = data.locations;
      var uiLocations = document.getElementById("uiLocations");
      $('#uiLocations').empty();  // Clear existing options
      for (var i in locations) {
        var opt = new Option(locations[i]);  // Create a new option for each location
        $('#uiLocations').append(opt);  // Append option to the dropdown
      }
    }
  });
}

window.onload = onPageLoad;  // Ensure onPageLoad runs when the page is loaded

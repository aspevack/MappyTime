
function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), {
	});
	//data is defined by loading a geoJSON in the HTML page
	//map.data.addGeoJson(mapData);
  //console.log(mapData.length);
  function setMarkers(map) {
    for (var i = 0; i < mapData.length; i++) {
      var point = mapData[i];
      //console.log(mapData[i]);
      var marker = new google.maps.Marker({
        position: {lat: point[0],lng:point[1]},
        map:map,
      })
    }
  } 
  setMarkers(map)

  var bounds = new google.maps.LatLngBounds();

	//fit the map to the points in data
	// this creates an array of the locations of the datapoints, then uses the built in function fitBounds to fit the map to those points
	for (var i = 0; i < mapData.length; i++) {
    	a = mapData[i][0];
    	b = mapData[i][1];
    	//console.log(a,b)
   		point = new google.maps.LatLng(a, b);
    	bounds.extend(point);
	}
	map.fitBounds(bounds);
 
  
  	// When the user clicks, open an infowindow
  	// global infowindow
  	//var infowindow = new google.maps.InfoWindow();

  	// create a listener for click events, add info from the GeoJSON
  	// change "description" to variable name that we want to display
  	// map.data.addListener('click', function(event) {
   //    	var infoContent = event.feature.getProperty("description");
   //    	infowindow.setContent("<div style='width:150px; text-align: center;'>"+infoContent+"</div>");
   //    	infowindow.setPosition(event.feature.getGeometry().get());
   //    	infowindow.setOptions({pixelOffset: new google.maps.Size(0,-30)});
   //    	infowindow.open(map);
  	}


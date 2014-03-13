var map;
function initializeMap() {
	var mapOptions = {
		zoom: 12,
		center: new google.maps.LatLng(-34.397, 150.644)
	};
	map = new google.maps.Map(document.getElementById('map-canvas'),
		mapOptions);
}

function placeMap(lat, lng) {
	map.setCenter(new google.maps.LatLng(lat, lng));
}

function addLocation(loc) {
	var marker = new google.maps.Marker({
		position: new google.maps.LatLng(loc.lat, loc.lng),
		map: map,
		title: loc.name
	});
}

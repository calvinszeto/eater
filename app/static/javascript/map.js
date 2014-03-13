var map;
var bounds;
function initializeMap() {
	var mapOptions = {
		zoom: 12,
		center: new google.maps.LatLng(-34.397, 150.644)
	};
	map = new google.maps.Map(document.getElementById('map-canvas'),
		mapOptions);
	bounds = new google.maps.LatLngBounds();
}

function addLocation(loc) {
	pos = new google.maps.LatLng(loc.lat, loc.lng)
	var marker = new google.maps.Marker({
		position: pos,
		map: map,
		title: loc.name
	});
	bounds.extend(pos);
}

function panMap() {
	map.panToBounds(bounds);
}

function resetMap() {
	bounds = new google.maps.LatLngBounds();
}

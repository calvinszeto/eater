google.maps.event.addDomListener(window, 'load', initializeMap);
$(function() {
	$('a#locate').bind('click', function() {
		$.getJSON($SCRIPT_ROOT + '/_locate_nearest', {
			address: $('input[name="address"]').val(),
		}, function(data) {
			$("#result").text(data.results);
		});
		return false;
	});
});

var map;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {
            lat: -34.397,
            lng: 150.644
        },
        zoom: 16
    });

    let geocoder = new google.maps.Geocoder;

    var pos;
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };

            map.setCenter(pos);

            //Position Marker
            var image = 'imgs/hereicon.png';
            let currentMarker = new google.maps.Marker({
                position: pos,
                map: map,
                icon: image
            });

        });
    } else {
        handleLocationError(false, infoWindow, map.getCenter());
    }

    let marker = new google.maps.Marker({
        position: new google.maps.LatLng(45.423831, -75.681608),
        map: map,
        icon: 'https://i.imgur.com/XCXF71h.png'
    })

    var infowindow = new google.maps.InfoWindow({
        content: 'Book now lil nigga'
    });

    marker.addListener('click', function() {
        infowindow.open(map, marker);
    });

    $.get("https://4e2d7ec9.ngrok.io/cars", function(data, status) {
        for (var i = 0; i < data.length; i++) {
            let d = data[i];
            let lat = d["lat"]
            let lon = d["lon"]
            let markerLocation = {
                lat: lat,
                lng: lon
            };
            let marker = new google.maps.Marker({
                position: markerLocation,
                map: map,
                icon: 'https://i.imgur.com/XCXF71h.png'
            })
            let infoWindow = new google.maps.InfoWindow({
                content: d["year"] + " " + d["model"] + " " + d["colour"]
            })
            marker.addListener("click", function() {
                infoWindow.open(map, marker);
            });
        }
    })
}
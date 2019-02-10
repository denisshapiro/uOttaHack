var map;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {
            lat: -34.397,
            lng: 150.644
        },
        zoom: 16
    });
    console.log('yeet')

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
    console.log(marker)
}
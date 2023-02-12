function initMap() {
  // The location
  const location = { lat: 45.4009454, lng: -75.6496752 };
  // The map, centered at location
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 4,
    center: location,
  });
  const marker = new google.maps.Marker({
    position: location,
    map: map
  });



  // google.maps.event.addListener(map, 'click', function(event) {
  //   const result = [event.latLng.lat(), event.latLng.lng()];
  //   transition(result);
  // });
  //
  // google.maps.event.addEventListener(window, 'load', initialize);
  // var numDeltas = 100;
  // var delay = 10;
  // var i = 0;
  // var deltaLat;
  // var deltaLng;
  //
  // function moveMarker(lat, long){
  //   position[0] += deltaLat;
  //   position[1] += deltaLng;
  //   var latlng = new google.maps.LatLng(position[0], position[1]);
  //   marker.setTitle("Latitude:"+position[0]+" | Longitude:"+position[1]);
  //   marker.setPosition(latlng);
  //   if(i!==numDeltas){
  //       i++;
  //       setTimeout(moveMarker, delay);
  //   }
  // }
}

window.initMap = initMap;


//change marker image
// function initMap() {
//   const map = new google.maps.Map(document.getElementById("map"), {
//     zoom: 4,
//     center: { lat: -33, lng: 151 },
//   });
//   const image =
//     "https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png";
//   const beachMarker = new google.maps.Marker({
//     position: { lat: -33.89, lng: 151.274 },
//     map,
//     icon: image,
//   });
// }
//
// window.initMap = initMap;
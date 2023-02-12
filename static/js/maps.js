function initMap(x, y) {
  // The location
  const location = {lat: 45.376347, lng: -75.702771};
  // The map, centered at location
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 13,
    center: location,
  });
  const marker1 = new google.maps.Marker({
    position: location,
    map: map
  });
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
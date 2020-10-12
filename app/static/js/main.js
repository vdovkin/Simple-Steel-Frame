const form = document.getElementById("form");
const length = document.getElementById("length");
const step = document.getElementById("step");
const constructionType = document.getElementById("constructionType");
const buildingType = document.getElementById("buildingType");
const gLoad = document.getElementById("gLoad");
const qLoad = document.getElementById("qLoad");
const payload = document.getElementById("payload");

function MainBeam() {
  document.getElementById("MainImage").src = "/static/img/shema1.jpg";
}

function SecBeam() {
  document.getElementById("MainImage").src = "/static/img/shema2.jpg";
}

function Calculate() {
  document.getElementById("BeamImage").src = "/static/img/beam.png";
  document.getElementById("CommImage").src = "/static/img/communication.png";
}

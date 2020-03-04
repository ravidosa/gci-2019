const https = require('https');

https.get('https://opensky-network.org/api/states/all?icao24=3c6444', (resp) => {
  let data = '';

  resp.on('data', (chunk) => {
    data += chunk;
  });

  resp.on('end', () => {
    data = JSON.parse(data);
    console.log("Callsign " + data.states[0][1] + "originating from " + data.states[0][2]);
    console.log("Currently located at " + data.states[0][5] + ", " + data.states[0][6] + " with altitude " + data.states[0][7] + " ft");
    console.log("Heading " + data.states[0][10] + " degrees at " + data.states[0][9] + " m/s");
  });

}).on("error", (err) => {
  console.log("Error: " + err.message);
});

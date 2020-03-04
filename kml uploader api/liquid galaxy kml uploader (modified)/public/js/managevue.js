var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue.js!',
    kmlList: [],

  },
  methods: {
  },
  created() {
    var self = this
    return fetch('http://localhost:5430/kml/manage/list', {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(self.formPayload)
    }).then(res => res.json()).then(json => {
      self.kmlList = json.list
    })
  }
})

Vue.component('kml', {
  props: ['kml'],
  template:
  `<li>
    <button class="collapsible">{{ kml.name }}</button>
    <div class="content">
      <p width="100%">Path: {{ kml.path }}</p>
      <button class="small del">Delete KML</button>
      <button class="small set">Set as Current</button>
    </div>
  </li>`
})

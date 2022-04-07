<script>
import axios from 'axios';
const URL = 'http://localhost:8000/api/name/1';
export function getName() {
    //return axios.get(URL).then(response => response.data);
  return 'aboba';
}

export function updateName(name) {
  return axios.put(URL, name);
}

</script>
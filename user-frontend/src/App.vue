<template>
  <div>
    <div class="banner">
      <h1>Benutzerdaten</h1>
      <form v-on:submit.prevent="sendData">
        <label for="name">Name:</label>
        <input type="text" id="name" v-model="name">
        <label for="birthdate">Geburtsdatum:</label>
        <input type="date" id="birthdate" v-model="birthdate">
        <button type="submit">Speichern</button>
      </form>
      <br />
    </div>
    <div v-if="users.length === 0">
      <p>Keine Nutzer vorhanden.</p>
    </div>
    <table v-else>
      <thead>
        <tr>
          <th>Name</th>
          <th>Alter</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(user, index) in users" :key="index">
          <td>{{ user.name }}</td>
          <td>{{ user.age }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data() {
    return {
      name: '',
      birthdate: '',
      users: []
    }
  },
  methods: {
    async sendData() {
      try {
        const response = await axios.post('http://localhost:5000/age', {
          name: this.name,
          birthdate: this.birthdate
        });
        const user = response.data;
        this.users.push(user);
        // clear the form
        this.name = ''
        this.birthdate = ''
      } catch (error) {
        console.error(error);
      }
    },
     getUsers() {
      axios.get("http://localhost:5000/age")
        .then(response => {
          console.log(response.data);
          this.users = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
  },
  created() {
    this.getUsers();
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.banner {
  background-image: url(./assets/Verkehrsmittelmix_1655726497.png);
  background-size: cover;
}

form {
  background-color: #4F9C8F;
  padding: 20px;
  border-radius: 10px;
  margin: 0 auto;
  width: 50%;
  font-family: 'FF Fago','Fago','Calibri','Carlito',sans-serif;
}

input[type="text"], input[type="date"] {
  background-color: #B8CAC6;
  border: none;
  border-top-right-radius: 5px;
  border-top-left-radius: 5px;
  border-bottom: 3px solid #4F9C8F;
  margin-bottom: 20px;
  width: 90%;
  padding: 10px;
  font-size: 16px;
  border-bottom: 1px solid #095145;
  margin-bottom: 20px;
  position: relative;
}

input[type="text"]:after, input[type="date"]:after {
  content: "";
  position: absolute;
  width: 100%;
  height: 3px;
  background-color: #4F9C8F;
  bottom: -3px;
  left: 0;
  display: block;
}

input[type="submit"] {
  background-color: #4F9C8F;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
}

button[type="submit"] {
  border-radius: 25px;
  font-size: 18px;
  padding: 10px 25px;
  background-color: #056e5c;
  color: white;
  font-weight: bold;
  border: none;
  cursor: pointer;
}


table {
  background-color: #F2F2F2;
  border-collapse: collapse;
  border-radius: 5px;
  margin: 0 auto;
  width: 50%;
  font-family: 'FF Fago','Fago','Calibri','Carlito',sans-serif;
}

th, td {
  border: 1px solid #ddd;
  text-align: left;
  padding: 8px;
}

th {
  background-color: #4F9C8F;
  color: white;
  font-weight: bold;
}

</style>

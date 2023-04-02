<template>
  <div>
    <h1>Benutzerdaten</h1>
    <form v-on:submit.prevent="sendData">
      <label for="name">Name:</label>
      <input type="text" id="name" v-model="name">
      <label for="birthdate">Geburtsdatum:</label>
      <input type="date" id="birthdate" v-model="birthdate">
      <button type="submit">Speichern</button>
    </form>
    <table>
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
        console.log('I have been clicked');
        const response = await axios.post('http://localhost:5000/users', {
          name: this.name,
          birthdate: this.birthdate
        });
        const user = response.data;
        const age = this.calculateAge(user.birthdate);
        this.users.push({
          name: user.name,
          age: age,
        });
        console.log('I got here');
        // clear the form
        this.name = ''
        this.birthdate = ''
      } catch (error) {
        console.error(error);
      }
    },
    calculateAge(birthdate) {
      const today = new Date()
      const birth = new Date(birthdate)
      let age = today.getFullYear() - birth.getFullYear()
      const month = today.getMonth() - birth.getMonth()
      if (month < 0 || (month === 0 && today.getDate() < birth.getDate())) {
        age--
      }
      return age
    }
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
</style>

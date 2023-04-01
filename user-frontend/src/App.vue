<template>
  <div>
    <h1>Benutzerdaten</h1>
    <form>
      <label for="name">Name:</label>
      <input type="text" id="name" v-model="name">
      <label for="birthdate">Geburtsdatum:</label>
      <input type="date" id="birthdate" v-model="birthdate">
      <button type="submit" @click.prevent="submit">Absenden</button>
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
    submit() {
      const age = this.calculateAge(this.birthdate)
      this.users.push({ name: this.name, age })
      this.name = ''
      this.birthdate = ''
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

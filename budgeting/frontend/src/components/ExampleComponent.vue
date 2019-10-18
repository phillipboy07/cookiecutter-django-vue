<template>
  <div class="container">
    <h1>Cookiecutter Django Vue Testing</h1>
    <p align="center">
      <img src="https://i.imgur.com/SA8cjs8.png" />
    </p>
    <h3>Expenses</h3>
    <div v-for="(expense, i) in expenses" :key="i">
      <h4>{{ expense.name }}}</h4>
      <p>{{ expense.value }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "FirstComponent",
  data() {
    return {
      expenses: []
    };
  },
  mounted() {
    this.fetchExpenses();
  },
  methods: {
    fetchExpenses() {
      fetch("http://0.0.0.0:8000/api/buckets/expenses", {
        method: "GET",
        headers: {
          Accept: "application/json"
        }
      }).then(response => {
        if (response.ok) {
          response.json().then(json => {
            this.expenses = json;
          });
        }
      });
    }
  }
};
</script>

<style lang="scss" scoped>
h1 {
  text-align: left;
}
</style>

<template>
  <nav class="navbar">
    <div class="navbar-logo">
      <h1 class="navbar-title">Stocks App</h1>
    </div>
    <ul class="navbar-list">
      <li class="navbar-item">
        <router-link to="/TSLA" class="navbar-link">TSLA</router-link>
      </li>
      <li class="navbar-item">
        <router-link to="/AAPL" class="navbar-link">AAPL</router-link>
      </li>
      <li class="navbar-item">
        <router-link to="/GOOGL" class="navbar-link">GOOGL</router-link>
      </li>
    </ul>
  </nav>
</template>

<style scoped>
.navbar {
  background-color: #f2f2f2;
  padding: 10px;
  display: flex;
  align-items: center;
}

.navbar-logo {
  margin-right: 10px;
}

.navbar-title {
  font-size: 24px;
  font-weight: bold;
  margin: 0;
  padding: 0;
}

.navbar-list {
  list-style-type: none;
  margin: 0;
  padding: 0;
  display: flex;
}

.navbar-item {
  margin-right: 10px;
}

.navbar-link {
  text-decoration: none;
  color: #2277a8; /* Nice blue color */
  font-weight: bold;
  padding: 5px 10px;
  border-radius: 5px;
}

.navbar-link:hover {
  background-color: #ddd;
}
</style>

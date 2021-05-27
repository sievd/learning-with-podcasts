<template>
  <div id="header">
    <input type="search" placeholder="Search" />
    <div class="profile">
      <img :src="$auth.user.picture" />
      <span>{{ $auth.user.name }}</span>
      <span class="material-icons md-8">expand_more</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "Header",
};
</script>

<style scoped>
#header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 2em;
  font-size: 0.6em;
}

.profile {
  display: flex;
  align-items: center;
  gap: 0.5em;
}

.profile:hover {
  cursor: pointer;
}

img {
  max-width: 25px;
  border-radius: 50px;
  margin-right: 0.2em;
}

img:hover {
  cursor: pointer;
}

input {
  outline: none;
}

input[type="search"] {
  font-family: inherit;
  font-size: 100%;
  color: #67696b;
}

input[type="search"] {
  background: #1d1d1d
    url(https://static.tumblr.com/ftv85bp/MIXmud4tx/search-icon.png) no-repeat
    9px center;
  border: solid 1px #3a3a3a;
  padding: 9px 10px 9px 38px;
  width: 7em;
  border-radius: 10em;
  transition: all 0.5s;
}

input[type="search"]:focus {
  width: 10em;
  background-color: #fff;
  border-color: #448ecf;
  box-shadow: 0 0 5px rgba(109, 207, 246, 0.5);
}
</style>

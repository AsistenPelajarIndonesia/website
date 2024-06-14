<script setup lang="ts">
const isSidebarOpened = useState('isSidebarOpened')
let isUserLoggedOut= true
const closeSidebar = () => {
    isSidebarOpened.value = false
}
</script>

<template>
    <nav class="navbar">
            <NuxtLink to="/"><img class="logo" src="/icon.svg"alt="logo" /></NuxtLink>
            <nav class="wrapper">
                <ul class="navigation">
                    <NuxtLink class="navbar-item" to="/">Beranda</NuxtLink>
                    <NuxtLink class="navbar-item" to="/soal">Pembuat Soal</NuxtLink>
                    <NuxtLink class="navbar-item" to="/ai">Kumpulan AI</NuxtLink>
                    <NuxtLink class="navbar-item" to="/productivity">Produktifitas</NuxtLink>
                    <NuxtLink class="navbar-item" to="/personality-test">Tes Kepribadian</NuxtLink>
                    <NuxtLink class="navbar-item" to="/learning-path-test">Tes Jalur Belajar</NuxtLink>
                </ul>
                <ul class="login" v-show="isUserLoggedOut">
                    <NuxtLink to="/login" class="login-button">Masuk</NuxtLink> 
                    <NuxtLink to="/register" class="register-button">Daftar</NuxtLink> 
                </ul>
            </nav> 
            <div class="menu-button">
            <i class="ph ph-list" @click="isSidebarOpened = true"></i> 
            </div>
        <ul class="sidebar" v-show="isSidebarOpened">
            <i class="ph ph-x close-sidebar-icon" @click="isSidebarOpened = false"></i> 
            <NuxtLink class="sidebar-item" @click="closeSidebar" to="/">Beranda</NuxtLink>
            <NuxtLink class="sidebar-item" @click="closeSidebar" to="/ai">Kumpulan AI</NuxtLink>
            <NuxtLink class="sidebar-item" @click="closeSidebar" to="/productivity">Produktifitas</NuxtLink>
            <NuxtLink class="sidebar-item" @click="closeSidebar" to="/personality-test">Tes Kepribadian</NuxtLink>
            <NuxtLink class="sidebar-item" @click="closeSidebar" to="/learning-path-test">Tes Jalur Belajar</NuxtLink>
            <hr class="sidebar-divider">
            <section v-show="isUserLoggedOut">
                <NuxtLink class="sidebar-item" to="/login">Masuk</NuxtLink>
                <NuxtLink class="sidebar-item" to="/register">Daftar</NuxtLink>
            </section>
        </ul>  
    </nav>
</template>

<style scoped>
.close-sidebar-icon {
    font-size: 35px;
    color: white;
}
.sidebar-divider {
    width: 100%;
    margin-top: 1rem;
    margin-bottom: 1rem;
}
.navbar {
    font-family: sans-serif;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 20px;
    padding: 15px;
    height: 60px;
    background-color: #222;
    box-shadow: 0 7px 15px 0 rgba(0, 0, 0, 0.5);
    position: sticky;
    top: 0;
    z-index: 999;
}

.navbar-item{
    list-style-type: none;
    padding: 15px;
    text-decoration: none;
    color: #fff;
    font-size: 20px;
    text-transform: capitalize;
}
.sidebar{
    top: 0;
    right: 0;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    position: fixed;
    height: 100vh;
    width: 250px;
    z-index: 999;
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
}
.sidebar-item{
    list-style-type: none;
    padding: 15px;
    text-decoration: none;
    color: #fff;
    font-size: 25px;
    text-transform: capitalize;
}

.sidebar-item:hover{
    color: crimson;
    transition: all .3s ease-in-out;
}

.wrapper{
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 20px;
    width: 100%;
    height: 30px;
}

.brand{
    display: flex;
    flex-direction: row;
    font-size: 1.5em;
    padding: 15px;
    text-transform: capitalize;
}

.login-button{
    list-style-type: none;
    text-decoration: none;
    padding: 10px;
    color: white;
    background-color: crimson;
}
.register-button {
    color: white;
    margin-left: 5px;
    border: 1px solid crimson;
    padding: 10px;
    font-size: 20px;
    text-decoration: none;
    text-transform: capitalize;
}

.register-button:hover {
    color: crimson;
    transition: all .3s ease-in-out
}


.logo {
    width: 50px;
    height: 50px;
    border-radius: 50px;
}


.active {
    background-color: crimson;
    color: white;
    padding: 10px;
}

.menu-button{
    display: none;
}

@media (max-width : 800px) {
    .wrapper{
        display: none;
    }

    .menu-button{
        display: block;
        color: #fff;
        font-size: 30px;
    }
}

@media (max-width : 400px) {
    .sidebar{
        width: 100%;
    }
}
</style>
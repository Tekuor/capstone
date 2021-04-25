<template>
    <div class="columns is-multiline is-centered">
        <div class="column has-text-centered is-12 header-text">
            <div>Casting actors just got simple!</div>
        </div>
        <div class="column has-text-centered is-12" style="margin-top: 48px;">
            <a class="button is-primary" @click="login">
                Sign up -- It's free
            </a>
        </div>
        <div class="column has-text-centered is-12">
            <div class="account-text"><a  @click="login"><span style="color:#FFFFFF">Already have an account?</span> <span style="color:#FFB733">Login</span></a></div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Movie',
        components: {
        },
        methods: {
            // Log the user out
            logout() {
                this.$auth.logout({
                    returnTo: window.location.origin
                });
            },
            login() {
                this.$auth.loginWithRedirect();
            }
        }
    }
</script>

<style scoped>
    @import url('https://fonts.googleapis.com/css2?family=Seaweed+Script&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif&display=swap');
    .header-text {
        font-family: Noto Serif;
        font-style: normal;
        font-weight: bold;
        font-size: 48px;
        line-height: 70px;
        text-align: center;
        letter-spacing: 0.05em;
        color: #FFFFFF;
        margin-top: 80px;
    }
    .header-div {
        width: 522px;
    }
    .button {
        background: #FFB733;
        border-radius: 8px;
        color: #131313;
        font-family: 'Noto Serif', serif;
        font-style: normal;
        font-weight: 900;
        font-size: 16px;
    }

    .nav-items {
        color: #FFFFFF;
        font-family: Noto Serif;
        font-style: normal;
        font-weight: normal;
        font-size: 14px;
    }
    .account-text {
        font-family: Noto Serif;
        font-style: normal;
        font-weight: normal;
        font-size: 14px;
        line-height: 19px;
        margin-top: 48px;
    }
</style>
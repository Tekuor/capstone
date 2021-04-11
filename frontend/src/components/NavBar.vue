<template>
    <b-navbar style="background-color:#990033">
        <template #end>
            <b-navbar-item href="#" class="has-text-grey-light">
                Movies
            </b-navbar-item>
            <b-navbar-item href="#" class="has-text-grey-light">
                Actors
            </b-navbar-item>
            <b-navbar-item tag="div">
                <div class="buttons">
                    <a class="button is-light" @click="logout">
                        Log out
                    </a>
                </div>
            </b-navbar-item>
        </template>
    </b-navbar>
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
            }
        }
    }
</script>
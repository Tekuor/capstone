<template>
    <div>
        <NavBar/>
        <div class="container columns">
            <div class="pt-4 px-4 column is-5 is-offset-4">
                <div class="is-size-4 py-5" style="color:#990033">Add Movie</div>
                <b-field label="Title">
                    <b-input v-model="form.title"></b-input>
                </b-field>

                <b-field label="Image Url">
                    <b-input v-model="form.image_url"></b-input>
                </b-field>

                <b-field label="Release Date" class="pb-5" >
                    <b-datetimepicker
                        v-model="form.release_date"
                        placeholder="Type or select a date..."
                        icon="calendar-today"
                        :locale="undefined"
                        editable>
                    </b-datetimepicker>
                </b-field>

                <b-button @click="addMovie()" type="is-primary" style="background-color:#990033">Add Movie</b-button>
            </div>
        </div>
    </div>
</template>

<script>
    import NavBar from "../components/NavBar";
    import axios from "axios";
    export default {
        name: 'Movie',
        components: {
            NavBar
        },
        data(){
            return {
                form: {
                    title: '',
                    image_url: '',
                    release_date: ''
                }
            }
        },
        methods: {
            // Log the user out
            logout() {
                this.$auth.logout({
                    returnTo: window.location.origin
                });
                localStorage.removeItem('token')
            },
            async addMovie() {
                this.$router.push('/movies')
                try{
                    // Get the access token from the auth wrapper
                    const token = await this.$auth.getTokenSilently();

                    // Use Axios to make a call to the API
                    await axios.post("http://127.0.0.1:5000/movies", this.form, {
                        headers: {
                        Authorization: `Bearer ${token}`    // send the access token through the 'Authorization' header
                        }
                    });
                }catch(e){
                    console.log(e)
                }
            }
        }
    }
</script>

<style scoped>

</style>
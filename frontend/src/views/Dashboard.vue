<template>
  <div class="home">
    <LoggedInNavBar/>

    <div class="columns is-multiline is-centered">
        <div style="padding-top: 70px; width: 70%;">
            <div class="card column is-12 first-div" style="height: 35%;">
                <div style="height: 100%;">
                    <div style="height: 100%;">
                        <div class="columns" style="height: 100%">
                            <div class="column is-3" style="height: 100%; padding-left: 40px; padding-top:20px">
                                <img  src="../assets/first_image.svg" style="height: 90%"/>
                            </div>
                            <div class="column has-text-centered is-6" style="height: 100%; padding-top:40px">
                                <div id="casting">Casting made easy</div>
                                <div id="casting-description">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</div>
                            </div>
                            <div class="column is-4 px-4" style="height: 100%;padding-top:20px">
                                <img  src="../assets/second_image.svg" style="height: 90%"/>
                            </div>
                        </div>    
                    </div>
                </div>
            </div>

            <div class="card column is-12 second-div" style="margin-top: 35px; height: 35%;">
                <div style="height: 100%; width:100%">
                        <div style="height: 100%">
                            <div class="columns" style="height: 100%">
                                <div class="column is-3" style="height: 100%">
                                   <img  src="../assets/third_image.svg" style="height: 100%"/>
                                </div>
                                <div class="column" style="height: 100%; padding-top:30px; padding-left:35px">
                                    <div class="title-text">Movie list - add movies</div>
                                    <div class="description-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</div>
                                    <div class="add-text"><a @click="addMovie()">Add Movies</a></div>
                                </div>
                            </div>
                        </div>
                </div>
            </div>

            <div class="card column is-12 third-div" style="margin-top: 35px; height: 35%;">
                <div style="height: 100%;">
                    <div style="height: 100%;">
                        <div class="columns" style="height: 100%">
                            <div class="column is-3" style="height: 100%">
                                <img  src="../assets/fourth_image.svg" style="height: 100%"/>
                            </div>
                            <div class="column" style="height: 100%; padding-top:30px; padding-left:35px">
                                <div class="title-text">Actors list - add actors</div>
                                <div class="description-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</div>
                                <div class="add-text">Add Actors</div>
                            </div>
                        </div>    
                    </div>
                </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import LoggedInNavBar from "../components/LoggedInNavBar";

export default {
  name: 'Home',
  components: {
    LoggedInNavBar
  },
  methods: {
    // Log the user in
    login() {
      this.$auth.loginWithRedirect();
    },
    addMovie(){
        this.$router.push('/add-movie')
    }
  }
}
</script>

<style scoped>
    .card {
        /* height: 200px; */
        border-radius: 8px;
        box-shadow: 0px 10px 50px rgba(4, 4, 4, 0.5);
        justify-content: center;
        align-items: center;    
    }

    .first-div {
        background: #FFEDCC;
    }

    .second-div {
        background: rgba(255, 255, 255, 0.1);
    }

    .third-div {
        background: rgba(255, 255, 255, 0.1);
    }

    .column {
        padding: 0px;
    }

    .title-text {
        font-family: Noto Serif;
        font-style: normal;
        font-weight: bold;
        font-size: 24px;
        line-height: 33px;
        color: #FFFFFF;
    }

    .description-text {
        font-family: Noto Serif;
        font-style: normal;
        font-weight: normal;
        font-size: 14px;
        line-height: 19px;
        color: #C2C2C2;
        padding-right: 40px;
        padding-top: 20px;
    }

    .add-text {
        font-family: Noto Serif;
        font-style: normal;
        font-weight: 900;
        font-size: 16px;
        line-height: 22px;
        color: #FFB733;
        padding-top: 20px;
    }

    #casting {
        font-family: Noto Serif;
        font-style: normal;
        font-weight: bold;
        font-size: 24px;
        line-height: 33px;
        text-align: center;
        color: #131313;
    }

    #casting-description {
        font-family: Noto Serif;
        font-style: normal;
        font-weight: normal;
        font-size: 14px;
        line-height: 19px;
        text-align: center;
        color: #131313;
    }
</style>
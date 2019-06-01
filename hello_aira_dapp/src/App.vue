<!--<template>
  <div id="app">
    <v-app id="inspire">
      <header role="banner">
        <div class="secw-narrow">
          <div id="header-logo">
            <a href="/">
              <img class="img-block" alt src="static/assets/i/logo.svg">
            </a>
          </div>
        </div>
      </header>
      <v-content>
        <v-container fluid grid-list-md>
          <v-layout row wrap>
            <v-flex md12>
              <web3-check>
                <div>
                  <router-view v-if="ready"/>
                  <div v-else>Initialization Robonomics</div>
                </div>
              </web3-check>
            </v-flex>
          </v-layout>
        </v-container>
      </v-content>
    </v-app>
  </div>
</template>
-->
<template>
  <div id="app">
    <v-app id="inspire">
      <v-content>
        <v-container grid-list-md style="margin: 18px auto 15px;">
          <v-layout justify-center row wrap>
            <v-flex sm12 md10 lg6>
              <v-layout row wrap>
                <v-flex xs12 sm6 class="text-xs-center text-sm-left">
                  <router-link to="/">
                    <img alt="" src="static/assets/i/logo.svg" style="height: 45px;"/>
                  </router-link>
                </v-flex>
                <v-flex xs12 sm6 class="text-xs-center text-sm-right">
                  <v-btn to="/" outline>Hello</v-btn>
                  <v-btn to="/trade" outline>Trade</v-btn>
                </v-flex>
              </v-layout>
            </v-flex>
          </v-layout>
        </v-container>
        <web3-check :networks="network" @changeNetwork="onChangeNetwork" @changeAccount="onChangeAccount">
          <router-view v-if="ready"/>
          <div v-else>Initialization Robonomics</div>
        </web3-check>
      </v-content>
    </v-app>
  </div>
</template>

<script>
import Vue from "vue";
import Web3Check from "vue-web3-check";
import { initRobonomics } from "./utils/robonomics";
import getIpfs from "./utils/ipfs";
import * as config from './config';

const network = Object.keys(config.ROBONOMICS).map((item) => {
  return Number(item)
})

export default {
  name: "app",
  data() {
    return {
      network: network,
      ready: false
    };
  },
  mounted() {
    Web3Check.store.on("load", state => {
      getIpfs().then(ipfs => {
        Vue.prototype.$robonomics = initRobonomics(ipfs, state.networkId);
        this.$robonomics.ready().then(() => {
          this.ready = true;
        });
      });
    });
  },
  methods: {
    onChangeNetwork (data) {
      if (data.check === true) {
        window.location.reload(false)
      }
    },
    onChangeAccount () {
      window.location.reload(false)
    }
  }
};
</script>

<style>
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 14px;
  line-height: 1.42857143;
  color: #333;
  background-color: #f2f2f2;
}
.application.theme--light {
  background: #f2f2f2;
  color: rgba(0, 0, 0, 0.87);
}
#header-logo .img-block {
  max-width: 400px;
}
.img-block {
  display: block;
  max-width: 100%;
  margin-left: auto;
  margin-right: auto;
}
.secw-narrow {
  max-width: 680px;
  padding-left: 20px;
  padding-right: 20px;
  margin: 0 auto;
}
header[role="banner"] {
  padding-top: 20px;
  padding-bottom: 40px;
}
.application .theme--light.card,
.theme--light .card {
  border: 1px solid #707070;
  border-radius: 0;
  box-shadow: none;
}
</style>

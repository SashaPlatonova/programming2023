<template>
<v-hover
    v-slot:default="{ hover }">
<v-card
   :elevation="hover? 15: 4"
   class = "px-2 py-5" :style = "{'background': 'linear-gradient(180deg, rgb(255, 255, 255) 90%, rgb(0, 71, 177) 24%)'}"
   @click="$router.push('/hostel/all' + hostelItem.id)
  $router.go()"
>
<v-row>
    <v-col class="mx-auto"
    v-if="hostelItem.address_id!=null">
      <v-card-title class="justify-center">
        {{ hostelItem.name}} {{ hostelItem.building}} {{ hostelItem.house_num }}
      </v-card-title>
     <v-card-text>
        {{ hostelItem.address_id }}
     </v-card-text>
   </v-col>
</v-row>
</v-card>
</v-hover>
</template>
<script>
export default {
  name: 'HostelCard',
  props: {
    hostelItem: Object
  }
}
</script>
<style>
v-card-title {
  text-align: center;
}
</style>

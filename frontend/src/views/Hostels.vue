<template>
<section>
  <h1>Hostels
    <v-btn
        color="warning"
        :style="{'margin':'20px'}"
        @click="$router.push('/hostels/create')
            $router.go()">
            Create
        </v-btn>
  </h1>
  <v-row>
    <v-col cols="6" class="mx-auto">
      <HostelCard
        v-for="hostelItem in hostelItems"
        :key="hostelItem.id"
        :hostel-item="hostelItem"
        class="my-2"
      />
    </v-col>
  </v-row>
</section>
</template>
<script>
import HostelCard from '@/components/HostelCard'
const apiURl = 'http://localhost:8000/api/hostels/all/?format=json'
export default {
  components: { HostelCard },
  name: 'Hostel',
  data: () => ({
    hostelItems: []
  }),
  methods: {
    async getHostel () {
      await this.axios.get(apiURl)
        .then(res => {
          this.hostelItems = res.data.Hostel
        })
        .catch(err => {
          console.log('error displaying subdivisionItems', err)
        })
    }
  },
  created () {
    this.getHostel()
  }
}
</script>
<style>
h1 {
  color: white;
  font-size: 32pt;
  text-shadow: 4px 4px 5px darkgray;
  margin: 3% 3%;
}
</style>

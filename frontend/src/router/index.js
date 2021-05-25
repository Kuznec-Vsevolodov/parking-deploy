import VueRouter from 'vue-router'
import Sectors from "@/components/Sectors"
import HelloWorld from "@/components/HelloWorld"
import Events from "@/components/Events"
import Places from "@/components/Places"
import SectorPage from "@/components/SectorPage";
import PlacePage from "@/components/PlacePage";
import LogIn from "@/components/LogIn";
import User from "@/components/User";
import RedPlace from "@/components/RedPlace";
import RedSector from "@/components/RedSector";

export default new VueRouter({
  mode: 'history',
  routes: [
      {
          path: '/sectors',
          component: Sectors
      },
      {
          path: '/',
          component: HelloWorld
      },
      {
          path: '/events',
          component: Events
      },
      {
          path: '/places',
          component: Places

      },
      {
          path: '/places/:id',
          component: PlacePage
      },
      {
          path: '/sectors/:id',
          component: SectorPage
      },
      {
          path: '/sectors/red-sectors/:id',
          component: RedSector
      },
      {
          path: '/login',
          component: LogIn
      },
      {
          path: '/profile/:id',
          component: User,
      },
      {
          path: '/places/red-places/:id',
          component: RedPlace,
      }
  ]
})
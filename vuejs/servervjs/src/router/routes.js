import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/Home.vue'
import NewGame from '../components/NewGame.vue'
import DeleteGame from '../components/DeleteGame.vue'
import UpdateGame from '../components/UpdateGame.vue'
import AllGames from '../components/AllGames.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/new_game',
        name: 'NewGame',
        component: NewGame
    },
    {
        path: '/delete_game',
        name: 'DeleteGame',
        component: DeleteGame
    },
    {
        path: '/update_game',
        name: 'UpdateGame',
        component: UpdateGame
    },
    {
        path: '/all_games',
        name: 'AllGames',
        component: AllGames
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
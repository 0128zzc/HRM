<template>
    <div id="sidebar" class="glass-panel">
        <header class="sidebar-header"><button id="toggle-sidebar" class='transparent theme' @click='toggleSidebar()'><span
                    class="icon" v-text="this.sidebarOpened ? '' : ''"></span></button></header>
        <ul class="sidebar-main">
            <template v-for="(route) in routes">
                <li v-if="route.meta.showInSidebar">
                    <router-link :to="route.path">
                        <span class="icon">{{ route.meta.icon }}</span><span class="title">{{ route.meta.title }}</span>
                    </router-link>
                </li>
            </template>
        </ul>
    </div>
</template>
<script>
import { routes } from '@/router'
export default {
    name: "SideBar",
    data() {
        return {
            routes: routes
        }
    },
    computed: {
        sidebarOpened() {
            return this.$store.state.app.sidebar.opened
        },
    },

    methods: {
        toggleSidebar() {
            this.$store.dispatch('app/toggleSidebar', { withAnimation: true });
        },

    }

}
</script>
<style scoped lang="scss">
@import "@/style/layout.scss";
@import "@/style/button.scss";


#sidebar {
    position: fixed;
    z-index: 3;
    top: 0;
    left: 0;
    width: $sidebar-width-full;
    height: 100vh;
    padding: 0 30px;
    border-top-right-radius: 20px;
    border-bottom-right-radius: 20px;

    .hideSidebar & {
        width: $sidebar-width-shrink;
    }
}



.sidebar-header {
    height: $topbar-height;
    line-height: $topbar-height;
    text-align: center;

    button#toggle-sidebar {
        font-size: 30px;
        vertical-align: middle;
    }
}

.sidebar-main {
    $sidebarItem-diameter: 2.8em;

    li {
        font-size: 16px;
        margin: 2em 0;
        white-space: nowrap;
        overflow: hidden;
    }

    a {
        display: inline-block;
        padding: 0 $sidebarItem-diameter / 4;
        width: 100%;
        height: $sidebarItem-diameter;
        line-height: $sidebarItem-diameter;
        border-radius: $sidebarItem-diameter / 2;
        transition: all 0.2s;

        .darkMode & {
            color: $d-sidebar-itemColor;
        }

        .lightMode & {
            color: $l-sidebar-itemColor;
        }

        .icon {
            font-size: $sidebarItem-diameter / 2;
            margin-right: 0.5em;
            filter: brightness(0.7);
        }

        .title {
            font-size: 0.9em;
            display: inline-block;
        }


        &:hover {

            .darkMode & {
                background-color: #{$d-sidebar-itemBgColor}11;
            }

            .lightMode & {
                background-color: #{$l-sidebar-itemBgColor}44;
            }
        }

        &.router-link-active {


            .darkMode & {
                color: $d-sidebar-itemColor-highlight;
                background-color: $d-sidebar-itemBgColor;
            }

            .lightMode & {
                color: $l-sidebar-itemColor-highlight;
                background-color: $l-sidebar-itemBgColor;

                .icon {
                    filter: brightness(1);
                }
            }
        }

    }
}
</style>

<template>
    <div id="layout" :class="globalClass">
        <div class="background-decorations">
            <div class="circle1"></div>
            <div class="circle2"></div>
            <div class="circle3"></div>
        </div>
        <div class="circle3"></div>
        <SideBar />
        <div class="mask" v-if="device === 'mobile' && sidebar.opened === true" @click="clickOutside()"></div>
        <TopBar />
        <main class="app-main">
            <router-view></router-view>
        </main>
    </div>
</template>


<script>
import SideBar from './SideBar.vue';
import TopBar from './topbar/index.vue';
import resizeHandler from './mixins/resizeHandler.js';
export default {
    name: "Layout",
    mixins: [resizeHandler],
    components: { SideBar, TopBar },
    computed: {
        sidebar() {
            return this.$store.state.app.sidebar;
        },
        device() {
            return this.$store.state.app.device;
        },
        globalClass() {
            return {
                darkMode: this.$store.state.app.mode === "dark",
                lightMode: this.$store.state.app.mode === "light",
                hideSidebar: !this.sidebar.opened,
                showSidebar: this.sidebar.opened,
                mobile: this.device === 'mobile',
                withAnimation: this.sidebar.withAnimation
            }
        }
    },
    methods: {
        clickOutside() {
            this.$store.dispatch('app/closeSidebar', { withAnimation: true });
        }
    }
}


</script>
<style scoped lang="scss">
@import "@/style/layout.scss";

#layout {
    width: 100vw;
    height: 100vh;

    &.darkMode {
        background-color: $d-app-background;
        color: white;
    }

    &.lightMode {
        background-color: $l-app-background;
    }
}

.app-main {
    width: 100vw;
    height: 100vh;
    padding-top: $topbar-height;
    padding-left: $sidebar-width-full + 30px;
    padding-right: 30px;
}

.withAnimation {

    .app-main,
    #sidebar,
    #topbar {
        transition: width 0.2s, padding-left 0.2s;
    }
}

.hideSidebar {
    .app-main {
        padding-left: $sidebar-width-shrink + 30px;
    }
}

//背景三个圆

.background-decorations {
    [class^="circle"] {
        position: fixed;
        border-radius: 100%;
        transition: all 0.2s;


        &:nth-child(1) {
            left: 200px;
            top: -40px;
            width: 100px;
            height: 100px;

            .darkMode & {
                background-color: $d-red;
            }

            .lightMode & {
                background-color: $l-red;
            }

            .hideSidebar & {
                transform: rotate(45deg) translate(-100px, 100px);
            }


        }


        &:nth-child(2) {

            bottom: -20px;
            left: -40px;
            width: 220px;
            height: 220px;

            .darkMode & {
                background-color: $d-yellow;
            }

            .lightMode & {
                background-color: $l-yellow;
            }

            .hideSidebar & {
                transform: rotate(-55deg) translate(-50px, -90px) scale(1.2);

            }

        }

        &:nth-child(3) {
            bottom: -20px;
            left: 100px;
            width: 130px;
            height: 130px;

            .darkMode & {
                background-color: $d-blue;
            }


            .lightMode & {
                background-color: $l-blue;
            }

            .hideSidebar & {
                transform: rotate(45deg) translate(-50px, 90px) scale(0.9);
            }
        }

    }
}

.mask {
    z-index: 2;
}
</style>

<template>
    <div id="topbar">

        <h2 class="title">{{ this.$route.matched[0].meta.title }}</h2>
        <ToggleModeBtn />
    </div>
</template>
<script>
import ToggleModeBtn from './components/ToggleModeBtn.vue'
export default {
    name: "TopBar",
    components: { ToggleModeBtn },
}
</script>
<style scoped lang="scss">
@import '@/style/layout.scss';

#topbar {
    position: absolute;
    z-index: 1;
    top: 0;
    right: 0;
    padding-left: 30px;
    width: calc(100vw - #{$sidebar-width-full});
    height: $topbar-height;
    line-height: $topbar-height;

    .hideSidebar & {
        width:calc(100vw - #{$sidebar-width-shrink});
    }

}

.title {
    position: relative;
    display: inline-block;
    font-size: 25px;

    .darkMode & {
        color: white;
    }


    .lightMode & {
        color: $l-topbar-titleColor;
    }
}
</style>

<template>
    <div id="toggle-mode">
        <button @click="toggleMode()"></button>
    </div>
</template>
<script>
export default {
    name: "ToggleModeBtn",
    methods: {
        toggleMode() {
            this.$store.dispatch('app/toggleMode');
        }
    },
    computed: {
        mode() {
            return this.$store.state.app.mode;
        }
    }

}
</script>
<style scoped lang='scss'>
@import '@/style/color.scss';

#toggle-mode {
    position: fixed;
    right: 20px;
    display: inline-block;
}

button {
    $circle-diameter: 23px;
    $padding: 3px;
    box-sizing: content-box;
    padding: $padding;
    position: relative;
    width: $circle-diameter * 3;
    height: $circle-diameter;
    line-height: $circle-diameter;
    border-radius: 1em;

    .darkMode & {
        background-color: #1e3160;
    }

    .lightMode & {
        background-color: #eee;
    }



    &::before {
        content: "";
        display: block;
        position: absolute;
        transition: left 0.2s;
        top: $padding;
        width: $circle-diameter;
        height: $circle-diameter;
        border-radius: 50%;

        .darkMode & {
            left: 2 * $circle-diameter + $padding;
            background-color: #fff;
        }

        .lightMode & {
            left: $padding;
            background-color: $l-red;
        }


    }

    &::after {
        font-family: 'icomoon';
        display: inline-block;
        position: absolute;
        top: $padding;
        font-size: $circle-diameter;

        .darkMode & {
            content: "";
            color: $d-yellow;
            left: $padding;
        }

        .lightMode & {
            content: "";
            color: $l-yellow;
            right: $padding;
        }
    }



}
</style>

const { body } = document;
const WIDTH = 992;

export default {
    methods: {
        $_isMobile() {
            const rect = body.getBoundingClientRect();
            return rect.width <= WIDTH;
        },
        $_resizeHandler() {
            const isMobile = this.$_isMobile();
            this.$store.dispatch('app/setDevice', isMobile ? 'mobile' : 'desktop');
            if (isMobile) {
                this.$store.dispatch('app/closeSidebar', { withAnimation: false });
            }
        }

    },
    beforeMount() {
        window.addEventListener('resize', this.$_resizeHandler);
    },
    beforeDestroy() {
        window.removeEventListener('resize', this.$_resizeHandler);
    },
    mounted() {
        if (this.$_isMobile()) {
            this.$store.dispatch('app/setDevice', 'mobile');
            this.$store.dispatch('app/closeSidebar', { withAnimation: false });
        }
    },



}
<template>
  <div class="introduction-container">
    <component :is="currentRole" />
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import adminIntroduction from './admin'
import editorIntroduction from './editor'

export default {
  name: 'ModelIntroduction',
  components: { adminIntroduction, editorIntroduction },
  data() {
    return {
      currentRole: 'adminIntroduction'
    }
  },
  computed: {
    ...mapGetters([
      'roles'
    ])
  },
  created() {
    if (!this.roles.includes('admin')) {
      this.currentRole = 'editorIntroduction'
    }
  }
}
</script>

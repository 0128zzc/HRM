<template>

     <div id="upload">
        <div class="basic-container"> 
            <button class="upload" >
                <img  :src="this.$store.state.app.mode =='dark'? require('../../assets/image/uploadDark.png') : require('../../assets/image/uploadLight.png')"
                alt="" width="100%" height="100%" />
            </button> 
            <div class="content">
                <input class="file" name="file" type="file" accept="file/pdf,image/gif,image/jpeg" @change="update"/>
            </div>
        </div> 
    </div>
</template>
<script>
export default {
    props: {
    // 值
    value: [String, Object, Array],
    // 大小限制(MB)
    fileSize: {
      type: Number,
      default: 2,
    },
    // 文件类型, 例如['png', 'jpg', 'jpeg']
    fileType: {
      type: Array,
      default: () => [".jpg", ".jpeg", ".png", ".doc", ".xls", ".xlsx", ".ppt", ".txt", ".pdf"],
    },
    // 是否显示提示
    isShowTip: {
      type: Boolean,
      default: true
    },
    // 单据id
    billId: {
      type: Number,
      require: true
    },
    // 单据类型
    billType: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      // 已选择文件列表
      fileList: [],
      // 是否显示文件上传弹窗
      visible: false,
      // 可上传的文件类型
      accept: '',
      action: 'action'
    };
  },
  created() {
    this.fileList = this.list
    // 拼接
    this.fileType.forEach(el => {
      this.accept += el
      this.accept += ','
    })
    this.fileType.slice(0, this.fileList.length - 2)
  },
    methods: {
      update(e){
        let file = e.target.files[0];
        let param = new FormData(); //创建form对象
        param.append('file',file);//通过append向form对象添加数据
        console.log(param.get('file')); //FormData私有类对象，访问不到，可以通过get判断值是否传进去
        // this.$axios.post('http://127.0.0.1:5000/upload',param,{headers:{'Content-Type':'application/x-www-form-urlencoded' }}, ) //请求头要为表单
        //   .then(response=>{
        //     console.log(response.data);
        //   })
        //   .catch(function (error) {
        //     console.log(error);
        //   })
      }
    }
//   
}
</script>
<style scoped>
.basic-container {
    left: 38%;
    top: 10%;
    width: 500px;
    height: 250px;
    position: absolute;
}
.upload {
    background-color: transparent;
    /* background-image: src="../../../public/image/upload.png"; */
    /* background-image: "./image/upload.png"; */
    left: 40%;
    top: 10%;
    width: 20%;
    height: 40%;
    position: relative;
}
.content{
    position: relative;
    top:16%;
    left: 40%;
}
</style>

<template>
    <div class="basic-container">
            <el-upload 
  drag
 :http-request="uploadFile"
 ref="uploadFile"
  accept=".pdf,.doc ,.png ,.jpg,.docx"
  :limit="fileLimit"
  :show-file-list="true"
  :file-list="fileList"
  :before-upload="beforeUpload"
  :on-change="onChange" 
  :on-success="uploadSuccess"
  multiple
  >
  <div class="el-upload__tip" slot="tip" style="font-size: 25px;">只能上传jpg/png文件，且不超过500kb</div>
  <el-button class="buttonStyle" size="small" type="primary" style="background-color: transparent; padding-top: 13%;">
        <img :src="this.$store.state.app.mode=='dark'?require('../../assets/images/dark.png'):require('../../assets/images/light.png')" style="background-color: transparent;width: 100%;height: 100%;">
    </el-button>
    <div class="el-upload__text" style="font-size: 25px;">将文件拖到此处，或<em>点击上传</em></div>
</el-upload>
    </div>

    
</template>
<script>
export default {
    data() {
      return {
        fileList:[],
        fileType: [ "pdf", "doc", "docx", "xls", "xlsx","txt","png","jpg", "bmp", "jpeg"],
        fileSize: 50,
        fileLimit: 300,
        formData:"",
        isShowProgress: false,
        customColor: '#910E0E',
        headers: { "Content-Type": "multipart/form-data" },

      }
    },
    mounted(){
      // this.$refs.uploadFile.$children[0].$refs.input.webkitdirectory = true;
    },
    methods: {
      delFile() {
      this.fileList = [];
    },
    handleChange(file, fileList) {
      this.fileList = fileList;
    },
    // uploadFile(file) {
    //   this.formData.append("file", file.file);
    // },
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    handlePreview(file) {
      console.log(file);
    },
    beforeUpload(file){
	if (file.type != "" || file.type != null || file.type != undefined){
	    //截取文件的后缀，判断文件类型
		const FileExt = file.name.replace(/.+\./, "").toLowerCase();
		//计算文件的大小
		const isLt5M = file.size / 1024 / 1024 < 50; //这里做文件大小限制
		//如果大于50M
		if (!isLt5M) {
			this.$showMessage('上传文件大小不能超过 50MB!');
			return false;
		}
		//如果文件类型不在允许上传的范围内
		if(this.fileType.includes(FileExt)){
			return true;
		}
		else {
			this.$message.error("上传文件格式不正确!");
			return false;
		}
	}
},
 uploadFile(item){
	//上传文件的需要formdata类型;所以要转
	let FormDatas = new FormData()
    FormDatas.append('file',item.file);
    console.log(FormDatas)
    console.log(item.file)
    console.log(this.fileList)
	this.$axios({
		method: 'post',
		url: '/file/fileUpload',
		headers:this.headers,
		timeout: 30000,
		data: FormDatas
		}).then(res=>{
			if(res.data.id != '' || res.data.id != null){
				this.fileList.push(item.file);//成功过后手动将文件添加到展示列表里
				let i = this.fileList.indexOf(item.file)
				this.fileList[i].id = res.data.id;//id也添加进去，最后整个大表单提交的时候需要的
				if(this.fileList.length > 0){//如果上传了附件就把校验规则给干掉
					this.fileflag = false;
					this.$set(this.rules.url,0,'')
				}
        uploadSuccess(response,item.file,this.fileList)
			}
		})
},
onChange(file, fileList) {
      console.log(fileList)
      this.fileList = fileList  //把当前文件赋值给 fileList 
    },
uploadSuccess: function(response, file, fileList) {
      if(response.meta.status==200){
        // console.log("文件上传成功",response)
        // this.$message.success(response.data.ProductFile.UploadOldName+"：文件上传成功");
        console.log(fileList)
        // console.log(file)
      }else{
        console.log("上传失败")
        // this.$message.error(response.data.ProductFile.UploadOldName+"：上传失败，请重新上传");
        //删除上传列表中，失败的文件
        let index = 0;
        for(const i in fileList){
          if(fileList[i]==file){
            index=i;
            break;
          }
        }
        //移出当前文件对象
        fileList.splice(index,1);
        // this.$refs.uploadFile.clearFiles();
      }
    },
    }
}
</script>
<style scoped>
.basic-container {
    width: 600px;
    height: 400px;
    position:absolute;
    left: 40%;
    top: 15%;

}
.buttonStyle{
    position: relative;
    padding-left: 0%;
}

.upload-demo  {
    width: 100%;
    height:100%;
    /* position: absolute; */

}
</style>

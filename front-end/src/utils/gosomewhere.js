
function goRemoteSense() {
    if (this.$route.path == "/remotesense") {
        this.$message.success("您已经在当前页面了哦");
    } else this.$router.push("remotesense");
}
function goIntelligent() {
    if (this.$route.path == "/intelligent") {
        this.$message.success("您已经在当前页面了哦");
    } else this.$router.push("intelligent");
}
function goTechnology() {
    if (this.$route.path == "/technology") {
        this.$message.success("您已经在当前页面了哦");
    } else this.$router.push("technology");
}
function goLogin() {
    if (this.$route.path == "/login") {
        this.$message.success("您已经在当前页面了哦");
    } else this.$router.push("login");
}
function goDetectChanges() {
    this.drawer = false
    if(!localStorage.getItem('token')){this.$message('请先登录哦~')}
    if (this.$route.path == "/detectchanges") {
        this.$message.success('您已经在该界面了哦')
    } else this.$router.push("detectchanges");
}
function goDetectTargets() {
    this.drawer = false;
    if(!localStorage.getItem('token')){this.$message('请先登录哦~')}
    if (this.$route.path == "/detecttargets") {
        this.$message.success('您已经在该界面了哦')
    } else this.$router.push("detecttargets");
}
function goObtainTargets() {
    this.drawer = false;
    if(!localStorage.getItem('token')){this.$message('请先登录哦~')}
    if (this.$route.path == "/obtaintargets") {
        this.$message.success('您已经在该界面了哦')
    } else this.$router.push("obtaintargets");
}
function goClassify() {
    this.drawer = false;
    if(!localStorage.getItem('token')){this.$message('请先登录哦~')}
    if (this.$route.path == "/classify") {
        this.$message.success('您已经在该界面了哦')
    } else this.$router.push("classify");
}
function goHistory() {
    if(!localStorage.getItem('token')){this.$message('请先登录哦~')}
    if (this.$route.path == "/history") { this.$message.success('您已经在该界面了哦') }
    else
        this.$router.push({
            name: "history",
  
        });
}
function goFeedBackHis() {
    if (this.$route.path == "/feedbackhistory") { this.$message.success('您已经在该界面了哦') }
    else this.$router.push({
        name: 'feedbackhistory',
    })
}
function goVisualData() {
    if (this.$route.path == "/visualdata") { this.$message.success('您已经在该界面了哦') }
    else this.$router.push("visualdata");
}



export {goRemoteSense, goIntelligent, goTechnology, goLogin, goDetectChanges, goDetectTargets, goObtainTargets, goClassify, goHistory, goFeedBackHis, goVisualData }

function answer(){
    return new Promise((res)=>{
        setTimeout(() => res("Answer it!"),4000)
    })
}
async function call(){
    console.log('calling')
    const res = await answer()
    console.log(res)

}
call()
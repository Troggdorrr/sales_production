"use strict";(self["webpackChunksales"]=self["webpackChunksales"]||[]).push([[325],{5580:function(t,s,r){r.d(s,{Z:function(){return h}});var e=r(3396);const o={class:"lds-ring"},a=(0,e._)("div",null,null,-1),i=(0,e._)("div",null,null,-1),c=(0,e._)("div",null,null,-1),n=(0,e._)("div",null,null,-1),u=[a,i,c,n];function d(t,s){return(0,e.wg)(),(0,e.iD)("div",o,u)}var p=r(89);const l={},_=(0,p.Z)(l,[["render",d]]);var h=_},3325:function(t,s,r){r.r(s),r.d(s,{default:function(){return st}});var e=r(3396);function o(t,s,r,o,a,i){const c=(0,e.up)("DetailProductCard"),n=(0,e.up)("SimiliarProducts");return(0,e.wg)(),(0,e.iD)(e.HY,null,[a.product?((0,e.wg)(),(0,e.j4)(c,{key:0,class:"product-detail container",product:a.product,shops:a.shops,isLastPage:a.isLastPage,onSeeMore:i.pushShops},null,8,["product","shops","isLastPage","onSeeMore"])):(0,e.kq)("",!0),a.product?((0,e.wg)(),(0,e.j4)(n,{key:1,class:"container",product_id:a.product.id},null,8,["product_id"])):(0,e.kq)("",!0)],64)}r(7658);var a=r(7139);const i={class:"detail-product"},c={class:"detail-product__section"},n={class:"detail-product__section"},u={class:"detail-product__title"},d={class:"detail-product__info-section"},p={class:"detail-product__price"},l={class:"detail-product__normal-price"},_={class:"detail-product__promo-price"},h={class:"primary-color"},g={class:"detail-product__info__attrs"},y=(0,e._)("span",{class:"detail-product__info__attrs__key"},"Ссылка на оригинальную страницу: ",-1),w={class:"primary-color"},m=["href"],k=(0,e._)("span",{class:"detail-product__info__attrs__key"},"Магазин: ",-1),P={class:"primary-color"},f=(0,e._)("span",{class:"detail-product__info__attrs__key"},"Тип акции: ",-1),L={class:"primary-color"},v=(0,e._)("span",{class:"detail-product__info__attrs__key"},"Дата начала акции: ",-1),S={class:"primary-color"},D=(0,e._)("span",{class:"detail-product__info__attrs__key"},"Дата конца акции: ",-1),C={class:"primary-color"},Z=(0,e._)("li",null,[(0,e._)("span",{class:"detail-product__info__attrs__key"},"Магазины в вашем городе: ")],-1),q={key:0,class:"detail-product__info__attrs nested"},z={class:"detail-product__info__attrs__key"},b=(0,e._)("span",{class:"detail-product__info__attrs__key primary-color"},"Найти ещё",-1),I=[b],$={key:1,class:"detail-product__info__attrs nested"},H=(0,e._)("li",null,[(0,e._)("span",{class:"detail-product__info__attrs__key"},"Магазинов не найдено")],-1),N=[H];function W(t,s,r,o,b,H){const W=(0,e.up)("ProductImage"),M=(0,e.up)("LikeIcon");return(0,e.wg)(),(0,e.iD)("div",i,[(0,e._)("div",c,[(0,e.Wm)(W,{src:r.product.poster,procentDiscount:H.procentDiscount,class:"detail-product__poster"},null,8,["src","procentDiscount"])]),(0,e._)("div",n,[(0,e._)("h1",u,(0,a.zw)(r.product.title),1),(0,e._)("div",d,[(0,e._)("div",p,[(0,e._)("p",l,(0,a.zw)(r.product.price)+"р.",1),(0,e._)("p",_,[(0,e._)("span",h,(0,a.zw)(r.product.promo_price),1),(0,e.Uk)("р. ")])]),(0,e.Wm)(M,{product:r.product,class:"detail-product__like__image"},null,8,["product"])]),(0,e._)("ul",g,[(0,e._)("li",null,[y,(0,e._)("span",w,[(0,e._)("a",{href:r.product.url,class:"primary-color",style:{"text-decoration":"none"}},(0,a.zw)(r.product.url),9,m)])]),(0,e._)("li",null,[k,(0,e._)("span",P,(0,a.zw)(r.product.donor.name),1)]),(0,e._)("li",null,[f,(0,e._)("span",L,(0,a.zw)(r.product.promo.type.name),1)]),(0,e._)("li",null,[v,(0,e._)("span",S,(0,a.zw)(r.product.promo.date_begin),1)]),(0,e._)("li",null,[D,(0,e._)("span",C,(0,a.zw)(r.product.promo.date_end),1)]),Z]),r.shops.length?((0,e.wg)(),(0,e.iD)("ul",q,[((0,e.wg)(!0),(0,e.iD)(e.HY,null,(0,e.Ko)(r.shops,(t=>((0,e.wg)(),(0,e.iD)("li",null,[(0,e._)("span",z,(0,a.zw)(t.address),1)])))),256)),r.isLastPage?(0,e.kq)("",!0):((0,e.wg)(),(0,e.iD)("li",{key:0,class:"detail-product__see-more",onClick:s[0]||(s[0]=s=>t.$emit("seeMore"))},I))])):((0,e.wg)(),(0,e.iD)("ul",$,N))])])}var M=r(5171),x=r(5336),j={components:{ProductImage:M.Z,LikeIcon:x.Z},emits:["seeMore"],props:{product:{type:Object,required:!0},shops:{type:Array,required:!0},isLastPage:{type:Boolean,required:!0}},computed:{procentDiscount(){return 100-Math.round(100*this.product.promo_price/this.product.price)}}},O=r(89);const R=(0,O.Z)(j,[["render",W]]);var T=R,E=r(9354),K=r(9242);const U={key:0,class:"last-page-info error-message"},Y={key:1,class:"network-error error-message"};function A(t,s,r,o,a,i){const c=(0,e.up)("Title"),n=(0,e.up)("ProductCardSet"),u=(0,e.up)("Loader");return(0,e.wg)(),(0,e.iD)("div",null,[(0,e.Wm)(c,{title:"Похожие товары"}),(0,e.Wm)(n,{class:"similiar-products__set",products:a.products},null,8,["products"]),(0,e.wy)((0,e.Wm)(u,{ref:"loader",class:"loader"},null,512),[[K.F8,a.isShowLoader]]),a.isLastPage?((0,e.wg)(),(0,e.iD)("p",U," Больше акций не найдено ")):(0,e.kq)("",!0),a.isHasNetwork?(0,e.kq)("",!0):((0,e.wg)(),(0,e.iD)("p",Y,[(0,e.Uk)(" Не удалось загрузить посты "),(0,e._)("span",{onClick:s[0]||(s[0]=s=>t.getPosts|(a.isShowLoader=!0)|(a.isHasNetwork=!0)),class:"network-error__button"}," Попробовать снова? ")]))])}var B=r(8862),F=r(5580),G=r(8448),J={components:{ProductCardSet:B.Z,Loader:F.Z,Title:G.Z},data(){return{products:[],isShowLoader:!0,isLastPage:!1,isHasNetwork:!0,page:1}},props:{product_id:{type:Number,required:!0}},methods:{async onLoaderInScreen(t){t[0].isIntersecting&&await this.pushProducts()},async pushProducts(){const t=await this.getProducts();t&&(this.products.push(...t),this.page+=1)},async getProducts(){try{const t=await E.Z.getSimiliar(this.product_id,{city:this.currentCity,page:this.page,is_expired:!1});return!t.next|!t.results.length&&(this.isLastPage=!0,this.isShowLoader=!1),t.results}catch(t){"ERR_NETWORK"==t.code?(this.isHasNetwork=!1,this.isShowLoader=!1):404===t.response.status&&(this.isLastPage=!0,this.isShowLoader=!1)}},reloadProducts(){this.products=[],this.page=1,this.isLastPage=!1,this.isShowLoader=!0}},mounted(){const t=new IntersectionObserver(this.onLoaderInScreen);t.observe(this.$refs.loader.$el)},computed:{currentCity(){return this.$store.state.currentCity?.id}},watch:{currentCity(t,s){this.reloadProducts()}}};const Q=(0,O.Z)(J,[["render",A]]);var V=Q,X={data(){return{product:void 0,isLastPage:!1,shops:[],page:1}},components:{DetailProductCard:T,SimiliarProducts:V},methods:{async setProduct(){this.product=await E.Z.getProduct(this.$route.params.pk)},async pushShops(){const t=await E.Z.getProductShops(this.$route.params.pk,{per_page:5,page:this.page,city:this.currentCity});t.next||(this.isLastPage=!0),this.shops.push(...t.results),this.page++}},async created(){await this.setProduct(),await this.pushShops()},computed:{currentCity(){return this.$store.state.currentCity?.id}},watch:{currentCity(t,s){this.shops=[],this.page=1,this.isLastPage=!1,this.pushShops()}}};const tt=(0,O.Z)(X,[["render",o]]);var st=tt}}]);
//# sourceMappingURL=325.c98abb6e.js.map
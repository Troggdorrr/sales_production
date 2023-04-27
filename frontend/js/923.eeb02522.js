"use strict";(self["webpackChunksales"]=self["webpackChunksales"]||[]).push([[923],{5580:function(t,e,r){r.d(e,{Z:function(){return h}});var o=r(3396);const s={class:"lds-ring"},i=(0,o._)("div",null,null,-1),a=(0,o._)("div",null,null,-1),p=(0,o._)("div",null,null,-1),n=(0,o._)("div",null,null,-1),u=[i,a,p,n];function l(t,e){return(0,o.wg)(),(0,o.iD)("div",s,u)}var c=r(89);const d={},_=(0,c.Z)(d,[["render",l]]);var h=_},923:function(t,e,r){r.r(e),r.d(e,{default:function(){return x}});var o=r(3396),s=r(9242);const i={class:"products container"},a={key:0,class:"last-page-info error-message"},p={key:1,class:"last-page-info error-message"},n={key:2,class:"network-error error-message"};function u(t,e,r,u,l,c){const d=(0,o.up)("Title"),_=(0,o.up)("ProductFilter"),h=(0,o.up)("ProductCardSet"),y=(0,o.up)("Loader");return(0,o.wg)(),(0,o.iD)("div",i,[(0,o.Wm)(d,{title:"Акции",description:"Список найденных скидок и акций"}),(0,o.Wm)(_,{onFilter_update:c.onFilterUpdate,price__gt:l.price__gt,"onUpdate:price__gt":e[0]||(e[0]=t=>l.price__gt=t),price__lt:l.price__lt,"onUpdate:price__lt":e[1]||(e[1]=t=>l.price__lt=t),search:l.search,"onUpdate:search":e[2]||(e[2]=t=>l.search=t),sort_by:l.sort_by,"onUpdate:sort_by":e[3]||(e[3]=t=>l.sort_by=t),promo_type:l.promo_type,"onUpdate:promo_type":e[4]||(e[4]=t=>l.promo_type=t),donor:l.donor,"onUpdate:donor":e[5]||(e[5]=t=>l.donor=t),promoTypes:l.promoTypes,donors:l.donors,class:"products__filter"},null,8,["onFilter_update","price__gt","price__lt","search","sort_by","promo_type","donor","promoTypes","donors"]),(0,o.Wm)(h,{products:l.products},null,8,["products"]),(0,o.wy)((0,o.Wm)(y,{ref:"loader",class:"loader"},null,512),[[s.F8,l.isShowLoader]]),l.isLastPage?((0,o.wg)(),(0,o.iD)("p",a," Больше акций не найдено ")):(0,o.kq)("",!0),l.isInvalidFilter?((0,o.wg)(),(0,o.iD)("p",p," Некорректный фильтр ")):(0,o.kq)("",!0),l.isHasNetwork?(0,o.kq)("",!0):((0,o.wg)(),(0,o.iD)("p",n,[(0,o.Uk)(" Не удалось загрузить акции "),(0,o._)("span",{onClick:e[6]||(e[6]=e=>t.getPosts|(l.isShowLoader=!0)|(l.isHasNetwork=!0)),class:"network-error__button"}," Попробовать снова? ")]))])}r(7658);var l=r(8862),c=r(9354),d=r(4161);const _={async getPromoTypes(){const t=await d.Z.get("/api/promotypes/");return t.data}};var h=_,y=r(5580),m=r(8448),g=r(7139);const v={class:"product-filter"},P=["value"],f=["value"],w=["value"],U=["value"],b=(0,o.uE)('<option value="" selected>Сортировать по...</option><option value="id">Дате добавления</option><option value="price">Цене</option><option value="promo_price">Цене по акции</option><option value="discount">Скидке</option><option value="-id">Дате добавления (От большей к меньшей)</option><option value="-price">Цене (От большей к меньшей)</option><option value="-promo_price">Цене по акции (От большей к меньшей)</option><option value="-discount">Скидке (От большей к меньшей)</option>',9),T=[b],$=["value"],L=(0,o._)("option",{value:"",selected:""},"Тип акции",-1),D=["value"],k=["value"],S=(0,o._)("option",{value:"",selected:""},"Магазин",-1),F=["value"];function I(t,e,r,s,i,a){return(0,o.wg)(),(0,o.iD)("div",v,[(0,o._)("input",{value:i.price__gt,onInput:e[0]||(e[0]=(...t)=>a.onUpdatePriceGT&&a.onUpdatePriceGT(...t)),placeholder:"Цена от",type:"number",name:"price__gt",class:"product-filter__input product-filter__mini-input"},null,40,P),(0,o._)("input",{value:i.price__lt,onInput:e[1]||(e[1]=(...t)=>a.onUpdatePriceLT&&a.onUpdatePriceLT(...t)),placeholder:"До",type:"number",name:"price__lt",class:"product-filter__input product-filter__mini-input"},null,40,f),(0,o._)("input",{value:i.search,onInput:e[2]||(e[2]=(...t)=>a.onUpdateSearch&&a.onUpdateSearch(...t)),placeholder:"Поиск по названию",name:"search",type:"text",class:"product-filter__input product-filter__big-input"},null,40,w),(0,o._)("select",{value:i.sort_by,onInput:e[3]||(e[3]=(...t)=>a.onUpdateSortBy&&a.onUpdateSortBy(...t)),name:"city",class:"product-filter__input product-filter__big-input"},T,40,U),(0,o._)("select",{value:i.promo_type,onInput:e[4]||(e[4]=(...t)=>a.onUpdatePromoType&&a.onUpdatePromoType(...t)),class:"product-filter__input product-filter__big-input"},[L,((0,o.wg)(!0),(0,o.iD)(o.HY,null,(0,o.Ko)(r.promoTypes,(t=>((0,o.wg)(),(0,o.iD)("option",{value:t.id},(0,g.zw)(t.name),9,D)))),256))],40,$),(0,o._)("select",{value:i.donor,onInput:e[5]||(e[5]=(...t)=>a.onUpdateDonor&&a.onUpdateDonor(...t)),class:"product-filter__input product-filter__big-input"},[S,((0,o.wg)(!0),(0,o.iD)(o.HY,null,(0,o.Ko)(r.donors,(t=>((0,o.wg)(),(0,o.iD)("option",{value:t.id},(0,g.zw)(t.name),9,F)))),256))],40,k)])}var q={data(){return{price__gt:"",price__lt:"",search:"",sort_by:"",promo_type:"",donor:""}},emits:["filter_update","update:price__lt","update:price__gt","update:search","update:sort_by","update:promo_type","update:donor"],props:{promoTypes:{type:Array,required:!0},donors:{type:Array,required:!0}},methods:{onUpdatePriceLT(t){this.price__lt=t.target.value,this.$emit("filter_update"),this.$emit("update:price__lt",t.target.value)},onUpdatePriceGT(t){this.price__gt=t.target.value,this.$emit("filter_update"),this.$emit("update:price__gt",t.target.value)},onUpdateSearch(t){this.search=t.target.value,this.$emit("filter_update"),this.$emit("update:search",t.target.value)},onUpdateSortBy(t){this.sort_by=t.target.value,this.$emit("filter_update"),this.$emit("update:sort_by",t.target.value)},onUpdatePromoType(t){this.promo_type=t.target.value,this.$emit("filter_update"),this.$emit("update:promo_type",t.target.value)},onUpdateDonor(t){this.donor=t.target.value,this.$emit("filter_update"),this.$emit("update:donor",t.target.value)}}},Z=r(89);const C=(0,Z.Z)(q,[["render",I]]);var H=C,N=r(8483),R={components:{ProductCardSet:l.Z,Loader:y.Z,Title:m.Z,ProductFilter:H},data(){return{products:[],page:1,isShowLoader:!0,isLastPage:!1,isHasNetwork:!0,isInvalidFilter:!1,promoTypes:[],donors:[],searchDelay:null,price__gt:"",price__lt:"",search:"",sort_by:"",promo_type:"",donor:""}},methods:{async onLoaderInScreen(t){t[0].isIntersecting&&await this.pushProducts()},async pushProducts(){const t=await this.getProducts();t&&(this.products.push(...t),this.page+=1)},async getProducts(){try{let t=Object.assign({page:this.page,city:this.currentCity,is_expired:!1},this.filterParams);const e=await c.Z.getProducts(t);return!e.next|!e.results.length&&(this.isLastPage=!0,this.isShowLoader=!1),e.results}catch(t){"ERR_NETWORK"==t.code?(this.isHasNetwork=!1,this.isShowLoader=!1):404===t.response.status?(this.isLastPage=!0,this.isShowLoader=!1):400===t.response.status&&(this.isShowLoader=!1,this.isInvalidFilter=!0)}},async pushPromoTypes(){this.promoTypes=await h.getPromoTypes()},async pushDonors(){this.donors=await N.Z.getDonors()},onFilterUpdate(){this.searchDelay&&(clearTimeout(this.searchDelay),this.searchDelay=null),this.searchDelay=setTimeout((()=>{this.isInvalidFilter=!1,this.reloadProducts(),this.setUrlParams()}),500)},reloadProducts(){this.products=[],this.page=1,this.isLastPage=!1,this.isShowLoader=!0},setUrlParams(){this.$router.replace({name:"products",query:this.filterParams})},setFilterFromUrlParams(){this.price__gt=this.$route.query.price__gt,this.price__lt=this.$route.query.price__lt,this.search=this.$route.query.search,this.sort_by=this.$route.query.sort_by,this.promo_type=this.$route.query.promo_type,this.donor=this.$route.query.donor}},mounted(){const t=new IntersectionObserver(this.onLoaderInScreen);t.observe(this.$refs.loader.$el)},created(){this.pushPromoTypes(),this.pushDonors(),this.setFilterFromUrlParams()},computed:{currentCity(){return this.$store.state.currentCity?.id},filterParams(){let t={};return this.price__gt&&(t.price__gt=this.price__gt),this.price__lt&&(t.price__lt=this.price__lt),this.search&&(t.search=this.search),this.sort_by&&(t.sort_by=this.sort_by),this.promo_type&&(t.promo_type=this.promo_type),this.donor&&(t.donor=this.donor),t},URLparams(){return this.$route.query}},watch:{currentCity(t,e){this.reloadProducts()},URLparams(t,e){this.setFilterFromUrlParams(),this.reloadProducts()}}};const W=(0,Z.Z)(R,[["render",u]]);var x=W}}]);
//# sourceMappingURL=923.eeb02522.js.map
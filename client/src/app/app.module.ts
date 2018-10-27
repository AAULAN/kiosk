import { ProductService } from './service/product.service';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './component/app.component';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ProductsOverviewComponent } from './component/products-overview/products-overview.component';
import { ProductDetailsComponent } from './component/product-details/product-details.component';

import { MatTableModule, MatButtonModule, MatIconModule, MatToolbarModule, MatCardModule, MatSnackBarModule } from '@angular/material';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { KeyInterceptor } from './interceptor/key.interceptor';

@NgModule({
  declarations: [
    AppComponent,
    ProductsOverviewComponent,
    ProductDetailsComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    MatTableModule,
    MatButtonModule,
    MatIconModule,
    MatToolbarModule,
    MatCardModule,
    HttpClientModule,
    MatSnackBarModule
  ],
  providers: [{provide: HTTP_INTERCEPTORS, useClass: KeyInterceptor, multi: true}],
  bootstrap: [AppComponent]
})
export class AppModule { }

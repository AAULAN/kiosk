import { ProductService } from './service/product.service';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './component/app.component';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ProductsOverviewComponent } from './component/products-overview/products-overview.component';
import { ProductDetailsComponent } from './component/product-details/product-details.component';

import { MatTableModule, MatButtonModule, MatIconModule, MatToolbarModule, MatCardModule } from '@angular/material';
import { HttpClientModule } from '@angular/common/http';

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
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

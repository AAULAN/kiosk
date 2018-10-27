import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ProductsOverviewComponent } from './products-overview/products-overview.component';
import { ProductDetailsComponent } from './product-details/product-details.component';

import { MatTableModule, MatButtonModule } from '@angular/material';

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
    MatButtonModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
